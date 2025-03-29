from perk import Perk

"""
TripleTap is a perk that refunds one round to the magazine for every three precision hits.

The actual perk reads:
Rapidly landing precision hits will return one round to the magazine.

A player must land 3 precision hits each within 2 seconds of each other for this perk to trigger.
When this perk triggers a round will be added to the magazine from thin air (meaning it does not consume ammo from reserves).

ENHANCED:
When enhanced, the window for landing precision hits increased from 2 to 3 seconds.

For the sake of testing it will be assumed that every hit is a precision hit and that the timing of the hits all fall within the required window.
"""

class TripleTap(Perk):
  """
  TripleTap is a perk that refunds one round to the magazine for every three precision hits.
  
  Attributes:
  - counter (int): Tracks the number of precision hits landed in sequence.
  - procs (int): Counts the number of times the perk has successfully triggered and refunded a round to the magazine.
  """
  def __init__(self, **kwargs):
    """
    Initializes a new instance of the TripleTap perk.
    """
    self.counter = 0
    self.procs = 0

  def shot_trigger(self, weapon):
    """
    Increment internal counter and check if the perk should proc.
    This method is called when a shot is fired from the weapon.
    """
    # Increment the counter for each hit
    self.counter += 1
    
    # Proc the perk if the counter reaches 3 and reset the counter
    if self.counter == 3:
      # Refund one round to the magazine and reset the counter
      weapon.magazine += 1
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
    Reports the current state of the TripleTap perk.
    This method prints out the number of times the perk has procced, and returns an object containing the report.
    """
    print("Triple Tap Procs: " + str(self.procs))
    print("Triple Tap Ammo Refunded: " + str(self.procs))
    print("Triple Tap Counter: " + str(self.counter))

    report = {
      "procs": self.procs,  # Number of times the perk has triggered
      "counter": self.counter,  # Current counter for precision hits
      "refunded": self.procs  # Number of rounds refunded (same as procs since each proc refunds one round)
    }

    return report

