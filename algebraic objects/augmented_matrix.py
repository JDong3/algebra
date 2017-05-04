from matrix import *
from vector import *

class AugmentedMatrix():
    """a class that represents an augmented matrix"""
    def __init__(self: 'AugmentedMatrix', source: Matrix,
                 augment: Vector or Matrix) -> None:
        self.source = source
        self.augment = augment
