from perk import Perk

class Weapon ():
  """
  A class that represents a simplified weapon in Destiny 2 for testing purposes.

  Attributes:
    - magazine_size: The size of the weapon's magazine.
    - fire_rate: The rate of fire of the weapon (rounds per second).
    - perks: A list of perks or modifiers that can affect the weapon's performance (e.g., Triple Tap).
    - reserves_size: The size of the reserves for the weapon. If -1, it indicates infinite reserves (primary ammo).
    - magazine: The current number of rounds in the magazine (initialized to magazine_size).
    - shots_fired: The number of shots fired from the magazine (initialized to 0).
    - reloads: The number of times the weapon has been reloaded (initialized to 0).
    - reserves: The current number of rounds in reserves (initialized to reserves_size).
  """
  
  def __init__(self, magazine_size: int = 0, fire_rate: int = 0, reserves_size: int = -1, perks: list[Perk] = []):
    """
    Initializes a new instance of the Weapon class.

    Parameters:
    - magazine_size (int): The size of the weapon's magazine (default is 0).
    - fire_rate (int): The rate of fire of the weapon in rounds per second (default is 0).
    - reserves_size (int): The size of the reserves for the weapon. If -1, it indicates infinite reserves (default is -1).
    - perks (list): A list of perks or modifiers that can affect the weapon's performance (default is an empty list).
    """
    # Weapon Attributes
    self.magazine_size = magazine_size
    self.fire_rate = fire_rate
    self.perks = perks
    self.reserves_size = reserves_size # Size of reserves, -1 means the weapon uses primary ammo (inifinte reserves)

    # Weapon State
    self.magazine = magazine_size # Initialize weapon with a full mag
    self.reserves = reserves_size # Initialize with full reserves
    self.shots_fired = 0
    self.reloads = 0


  def shoot(self):
    """
    Simulate firing a round from the weapon.
    Returns True if a round was successfully fired, False if the magazine is empty.
    """
    if self.magazine == 0: return False

    # Decrement the magazine count when firing the round
    self.magazine -= 1

    # Increment the shots fired counter
    self.shots_fired += 1

    # Apply perks or modifiers to the magazine if any
    for perk in self.perks:
      perk.shot_trigger(self)  # Call method on each perk to apply its on shot effect to the weapon

    return True


  def reload(self):
    """
    Simulates relodaing the weapon.
    Returns True if the weapon was successfully reloaded, False if there were no reserves to reload from.
    """
    # Check if reserves are available to reload from
    if self.reserves <= 0:
      return False
    
    # Calculate the amount to reload
    ammo_to_reload = self.magazine_size - self.magazine
    ammo_to_reload = min(ammo_to_reload, self.reserves)  # Ensure we don't reload more than available in reserves

    # Reload the magazine with ammo from reserves
    self.magazine += ammo_to_reload
    self.reserves -= ammo_to_reload  # Decrease reserves by the amount reloaded

    # Record that a reload has occurred
    self.reloads += 1

    # Call the method on each perk to trigger its reload check
    for perk in self.perks:
      perk.reload_trigger(self)  # Call method on each perk to apply its on reload effect to the weapon

    return True
  
  def resupply(self):
    """
    Resets the weapon to its initial state.
    """
    self.magazine = self.magazine_size
    self.reserves = self.reserves_size  # Reset reserves to initial size
    self.shots_fired = 0  # Reset shots fired counter
    self.reloads = 0  # Reset reloads counter

    for perk in self.perks:
      perk.reset()

  def report(self):
    """
    Prints a report of the weapon's current state, including magazine, reserves, shots fired, and reloads.
    Also calls the report method on each perk to display their individual states.
    Returns an object that contains the current state of the weapon and its perks.
    """
    # Calculate extra shots fired

    print(f"Magazine: {self.magazine}/{self.magazine_size}")
    print(f"Reserves: {self.reserves}/{self.reserves_size}")
    print(f"Shots Fired: {self.shots_fired}")
    print(f"Reloads: {self.reloads}")


    # Collect the report from each perk to include in the final report
    perk_states = {}

    for perk in self.perks:
      perk_states[perk.__class__.__name__] = perk.report()

    # Return an object with the current state of the weapon and its perks for further use if needed
    report = {
      "magazine": self.magazine,
      "magazine_size": self.magazine_size,
      "reserves": self.reserves,
      "shots_fired": self.shots_fired,
      "reloads": self.reloads,
      "perks": perk_states
    }

    return report

    

    