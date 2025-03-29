from perk import Perk
import math

"""
RewindRounds is a perk that refunds rounds to the magazine from reserves for every hit landed while the perk is active.
It has somewhat nasty conditions tied into it.

The actual perk reads:
When this weapon's magazine is empty, it refills from reserves based on the number of hits.

This perk keeps track of every hit from the weapon.
Upon the magazine reaching 0, it will CONDITIONALLY refund 60% of the hits landed (rounded up) back to the magazine from reserves.
It also cannot overfill the magazine, meaning if there are other perks or modifiers that add back to the magazine, it will never add more than the magazine size back to the magazine.
This refund is conditional upon the count of hits landed being >= 28.75% of the magazine size (rounded up) before the magazine reaches 0.
 - If the magazine size is 100, then 28.75% of that is 28.75 rounds, which rounds up to 29 rounds. This means you need to land 29 hits before the magazine reaches 0 to proc the refund.

This perk's counter starts counting starting from either:
- The last reload
- The last proc of the perk

While the former is simple, the later of these starting points adds another layer of complexity.
When this perks procs there is approximately 1 second of time the perk becomes inactive.

This means that for the first proc the hit calculation is simple, just count the number of shots.
For each subsequent proc, the calculation will require the use of a "disabled shots" which 
will be equal to the RPM (rounds per minute) of the wepon divided by 60 (to get the shots per second),
rounded down, to determine how many shots were fired during the time the perk was inactive.

SPECIAL CONSIDERATIONS:
On top of all of this, there is special consideration to be made IF the weapon is an Adaptive Burst Fire Linear Fusion Rifle.
In this case, each individual bolt from the burst counts as a hit (meaning for each 'shot' there are multiple hits registered for this perk).
It also means that the percentage of the refund is lowered to account for the increase in hits landed per shot from %60 to %14.
Because Adaptive Burst Fire Linear Fusion Rifles are a special case and make up a small portion of the weapons in the game, this is a special case WILL BE IGNORED.

ENHANCED:
Refills 70% of hits instead of 60%.
For Adaptive Burst Fire Linear Fusion Rifles this is 16.33% instead of 14%.
"""

class RewindRounds(Perk):
  """
  RewindRounds is a perk that refunds rounds to the magazine from reserves based on the number of hits landed while the perk is active.
  
  Attributes:
  - counter (int): Tracks the number of hits landed since the last reload or perk proc.
  - procs (int): Counts the number of times the perk has successfully triggered and refunded rounds to the magazine.
  - refunded (int): Total rounds refunded to the magazine from reserves.
  - percentage_refund (float): The percentage of hits refunded to the magazine. This is 60% by default, or 70% if enhanced.
  - disabled_shots (int): The number of shots fired during the perk's inactive period (used for subsequent procs). This is calculated based on the weapon's RPM divided by 60 to get shots per second.
  """
  def __init__(self, enhanced: bool = False):
    """
    Initializes a new instance of the RewindRounds perk.

    Parameters:
    - enhanced (bool): Indicates whether this perk is in its enhanced state. Default is False.
    """
    super().__init__(enhanced)
    self.counter = 0  # Counter for tracking hits landed
    self.procs = 0  # Number of times the perk has triggered
    self.refunded = 0  # Total rounds refunded to the magazine from reserves
    self.percentage_refund = 0.7 if enhanced else 0.6
    self.disabled_shots = 0 # Number of shots fired during the perk's inactive period (used for subsequent procs)

  def shot_trigger(self, weapon):
    """
    Check the conditionals for the perk and increment the counter.
    If the perk conditions are met, refund rounds to the magazine from reserves.
    This method is called when a shot is fired from the weapon.
    """
    # Check if the shot was fired during a time the perk was inactive
    if (self.disabled_shots > 0):
      self.disabled_shots -= 1
      return

    # Increment the hits
    self.counter += 1

    # If the magazine is empty check the condition for refund
    if (weapon.magazine == 0):
      # Calculate the activation threshold based on the magazine size
      activation_threshold = max(1, math.floor(weapon.magazine_size * 0.2875))

      # Check if the counter exceeds the activation threshold
      if (self.counter >= activation_threshold):
        print("Counter: " + str(self.counter) + " | Activation Threshold: " + str(activation_threshold))
        # Calculate potential refund based on the current counter
        potential_refund = math.ceil(self.counter * self.percentage_refund)

        # Calculate actual refund based on resereves
        actual_refund = min(potential_refund, weapon.reserves)

        # Ensure magazine size limit for refund
        refund = min(actual_refund, weapon.magazine_size)
        print("Refund: ", refund)

        # Update the magazine and reserves
        weapon.magazine += refund
        weapon.reserves -= refund

        # Update the refunded count
        self.refunded += refund
        self.procs += 1

        # Reset the counter after proc and set up for next calculation
        self.counter = 0
        self.disabled_shots = math.floor(weapon.fire_rate // 60)


  def reload_trigger(self):
    """
    Trigger effects when the weapon is reloaded.
    Rewind rounds is reset by a reload.
    """
    self.counter = 0
    self.disabled_shots = 0 # Reset the disabled shots on reload

  
  def reset(self):
    """
    Resets the perk.
    """
    self.counter = 0
    self.procs = 0
    self.refunded = 0
    self.disabled_shots = 0


  def report(self):
    """
    Reports the current state of the RewindRounds perk.
    This function prints out the stats for the perk and returns a dictionary with the current state.
    """

    print("Rewind Rounds Procs: " + str(self.procs))
    print("Rewind Rounds Refunded: " + str(self.refunded))
    print("Rewind Rounds Counter: " + str(self.counter))
    print("Rewind Rounds Disabled Shots: " + str(self.disabled_shots))
    
    report = {
      "procs": self.procs,  # Number of times the perk has triggered
      "refunded": self.refunded,  # Total rounds refunded to the magazine from reserves
      "counter": self.counter,  # Current counter for hits landed
      "disabled_shots": self.disabled_shots  # Remaining disabled shots (shots fired during the perk's inactive period)
    }

    