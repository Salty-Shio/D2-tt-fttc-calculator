from perk import Perk

"""
FourthTimesTheCharm is a perk that refunds two rounds to the magazine for every four precision hits.

The actual perk reads:
Rapidly landing precision hits will return two rounds to the magazine.

A player must land 4 precision hits each within 2 seconds of each other for this perk to trigger.
When this perk triggers, two rounds will be added to the magazine from thin air (meaning it does not consume ammo from reserves).

ENHANCED:
When enhanced, the window for landing precision hits increased from 2 to 3 seconds.

For the sake of testing, it will be assumed that every hit is a precision hit and that the timing of the hits all fall within the required window.
"""

class FourthTimesTheCharm(Perk):
  """
  FourthTimesTheCharm is a perk that refunds two rounds to the magazine for every four precision hits.
  
  Attributes:
  - counter (int): Tracks the number of precision hits landed in sequence.
  - procs (int): Counts the number of times the perk has successfully triggered and refunded two rounds to the magazine.
  """
  def __init__(self, **kwargs):
    """
    Initializes a new instance of the FourthTimesTheCharm perk.
    """
    self.counter = 0  # Counter for tracking precision hits
    self.procs = 0  # Number of times the perk has triggered
  
  def shot_trigger(self, weapon):
    """
    Increment internal counter and check if the perk should proc.
    This method is called when a shot is fired from the weapon.
    """
    # Increment the counter for each hit
    self.counter += 1
    
    # Proc the perk if the counter reaches 4 and reset the counter
    if self.counter == 4:
      # Refund two rounds to the magazine and reset the counter
      weapon.magazine += 2
      self.counter = 0

      # Record the proc
      self.procs += 1

  def reset(self):
    """
    Resets the counter and procs for the perk.
    """
    self.counter = 0
    self.procs = 0

  def report(self):
    """
    Report the number of times the perk has triggered and refunded rounds.
    This method can be used to display the performance of the perk.
    """
    print("Fourth Times The Charm Procs: " + str(self.procs))
    print("Fourth Times The Charm Refunded: " + str(self.procs * 2))  # Each proc refunds 2 rounds
    print("Fourth Times The Charm Counter: " + str(self.counter))  # Show current counter for debugging purposes

    report = {
      "procs": self.procs,  # Number of times the perk has triggered
      "refunded": self.procs * 2,  # Total rounds refunded (2 rounds per proc)
      "counter": self.counter  # Current counter for precision hits
    }

    return report