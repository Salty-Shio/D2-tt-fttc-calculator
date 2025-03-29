from typing import Optional

from weapon import Weapon
from firingRange import FiringRange
from perks import TripleTap, FourthTimesTheCharm, RewindRounds
from perk import Perk


def main():
  # Get the user to define a weapon configuration.
  current_weapon = define_weapon()
  
  # Main Loop for running tests on the weapon.
  while True:
    print("\nSelect an option:")
    print("1: Magazine Test")
    print("2: All Ammo Test")
    print("3: Both Tests")
    print("4: Make new Weapon")
    print("5: Exit")

    test_type = get_valid_text_input("Enter your choice (1-5): ", ['1', '2', '3', '4', '5'])

    # Handle exit case
    if test_type == '5':
      print("Exiting the test.")
      break

    # Handle creation of new weapon configuration
    if test_type == '4':
      print("Creating a new weapon configuration.")
      current_weapon = define_weapon()  # Allow user to define a new weapon
      pass

    # Run the selected test(s)
    run_test(current_weapon, test_type)
    


def define_weapon():
  """
  Gets a user defined weapon configuration. 
  """

  # Get basic weapon parameters.
  magazine_size = get_valid_int_input("Enter magazine size: ", min_value=1, max_value=300)
  reserves_size = get_valid_int_input("Enter reserves size (enter -1 for infinite reserves): ", min_value=-1, max_value=10000)

  # Get perks from user.
  perks = []
  perk_one_selection = get_valid_text_input("Select first perk:\n 1: Triple Tap\n 2: Fourth Times the Charm\n 3: Rewind Rounds\n 4: None\n Perk Selection: ", ['1', '2', '3', '4'])
  perk_one_enhanced = True if get_valid_text_input("\nIs the first perk enhanced? (y/n): ", ['y', 'n']) == 'y' else False
  perk_two_selection = get_valid_text_input("\nSelect second perk:\n 1: Triple Tap\n 2: Fourth Times the Charm\n 3: Rewind Rounds\n 4: None\n Perk Selection: ", ['1', '2', '3', '4'])
  perk_two_enhanced = True if get_valid_text_input("\nIs the second perk enhanced? (y/n): ", ['y', 'n']) == 'y' else False
  
  perks.append(return_perk(perk_one_selection, perk_one_enhanced))
  perks.append(return_perk(perk_two_selection, perk_two_enhanced))

  fire_rate = 0  # Default fire rate, will be set if rewind rounds is selected.
  # If rewind rounds is selected, ensure that the user provides the fire rate of the weapon.
  if (perk_one_selection == '3' or perk_two_selection == '3'):
    fire_rate = get_valid_int_input("Enter the fire rate of the weapon (rounds per minute): ", min_value=1, max_value=1000)

  # Create the weapon object with the specified parameters.
  return Weapon(magazine_size=magazine_size, fire_rate=fire_rate, reserves_size=reserves_size, perks=perks)

def return_perk(selection: str, is_enhanced: bool):
  """
  Helper function that returns a perk object based on the user's selection.
  """
  match selection:
    case '1':
      # Triple Tap perk
      return TripleTap(enhanced=is_enhanced)
    case '2':
      # Fourth Times the Charm perk
      return FourthTimesTheCharm(enhanced=is_enhanced)
    case '3':
      # Rewind Rounds perk
      return RewindRounds(enhanced=is_enhanced)
    case '4':
      # No perk selected
      return Perk()

def run_test(weapon, test_type):
  """
  Runs the user specified test.
  """
  match test_type:
    case '1':
      # Run Magazine Test
      FiringRange.mag_test(weapon)
    case '2':
      # All ammo test
      FiringRange.all_ammo_test(weapon)
    case '3':
      # Both Tests
      FiringRange.mag_test(weapon)
      FiringRange.all_ammo_test(weapon)

def get_valid_text_input(prompt: str, valid_options: list):
  """
  Helper function to get valid input from the user for test selection.
  """
  while True:
    user_input = input(prompt).strip().lower()
    if user_input in valid_options:
      return user_input
    else:
      print(f"\nInvalid input. Please enter one of the following: {', '.join(valid_options)}")
      continue

def get_valid_int_input(prompt: str, min_value: Optional[int] = None, max_value:Optional[int] = None):
  """
  Helper function to get a valid integer input from the user within optional min and max values.
  """
  while True:
    try:
      user_input = int(input(prompt).strip())
      if (min_value is not None and user_input < min_value) or (max_value is not None and user_input > max_value):
        print(f"\nInput must be between {min_value} and {max_value}. Please try again.")
        continue
      return user_input
    except ValueError:
      print("Invalid input. Please enter a valid integer.")
      continue


if __name__ == '__main__':
    main()