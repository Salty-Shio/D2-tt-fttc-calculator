from weapon import Weapon

class FiringRange():
  """
  A class that holds the methods for simulating the tests for firing the weapons.
  """

  def mag_test(weapon: Weapon):
    """
    Tests Firing one magazine of a weapon.
    - Weapon: The weapon object to be tested.
    """
    # Fire the weapon until the magazine is empty
    print("\nMAGAZINE TEST")
    
    # Fire the weapon until the magazine is empty
    remaining_ammo = True
    while (remaining_ammo):
      remaining_ammo = weapon.shoot()

    # Report the status of the weapon after using the magazine
    weapon.report()

    # Determine the number of shots fired and compare to the magazine size
    print("Extra Shots Fired: " + str(weapon.shots_fired - weapon.magazine_size))
    print("\nMagazine test completed.\n")

    weapon.resupply()

  def all_ammo_test(weapon: Weapon):
    """
    Tests expending all ammo from a weapon.

    Parameters:
    - weapon: The weapon object to be tested.
    """

    # Exit test if the weapon has infinite reserves.
    if weapon.reserves_size == -1:
      print ("This weapon uses primary ammo meaning it has infinite reserves. Cannot test all ammo.")
      return
    
    print("\nALL AMMO TEST")
    # Fire the weapon until the magazine and reserves are empty.
    remaining_ammo = True
    while (remaining_ammo):
      # Attempt to fire the weapon
      shot_fired = weapon.shoot()
      
      # If the weapon cannot fire (magazine is empty), attempt to reload
      if not shot_fired:
        successful_reload = weapon.reload()

        # If reload was unsuccessful, there is no ammo left to fire
        if not successful_reload:
          remaining_ammo = False
          print("No more ammo left to fire.")

    # Report the status of the weapon after expending all ammo
    weapon.report()
    print("Total Initial Ammo: " + str(weapon.magazine_size + (weapon.reserves_size)))
    print("Extra Shots Fired: " + str(weapon.shots_fired - (weapon.magazine_size + weapon.reserves_size)))
    print("\nAll ammo test completed.\n")

    weapon.resupply()