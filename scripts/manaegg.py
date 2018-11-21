class ManaEgg(object):
    """
    The central class representing a Mana Egg

    Parameters
    ----------
    egg_name : str
        A string containing an Egg Name, e.g. "Flare"

    Attributes
    ----------
    min_cost : int
        The minimum cost of this egg.

    child_junctions : int[]
        The child junctions of this egg.
    """

    min_cost = -1
    child_junctions = []

    def __init__(self, egg_name):
        self.egg_name = egg_name