

class  Perk():
  """
  Parent class for perks or modifiers that can be applied to a weapon.
  This class provides a template for defining perks that can modify the behavior of a weapon when firing or reloading.
  """
  def __init__(self, enhanced: bool = False):
    """
    Initializes a new instance of the Perk class.
    Parameters:
    - enhanced (bool): Indicates whether this perk is in its enhanced state. Default is False.
    """
    self.enhanced = enhanced  # Indicates if the perk is enhanced.
    pass

  def shot_trigger(self, weapon):
    pass

  def reload_trigger(self, weapon):
    pass

  def reset(self):
    pass

  def report(self):
    pass