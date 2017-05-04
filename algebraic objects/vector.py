"""representing vectors from a functional perspective"""
from fractions import Fraction
import copy
'''
restructuring Vector
algorithms with Fraction object
implementation of data[0]
'''


class Vector():
    """a class that represents a mathematical vector"""
    def __init__(self: 'Vector', data: list) -> None:
        self.data = data
        self.length = len(self.data)

    def __str__(self: 'Vector') -> str:
        return str(self.data[0])

    def __add__(self: 'Vector', v: 'Vector') -> 'Vector' or None:
        """
        :param v: is a vector object
        :return: the sum of self and another vector object
        """
        if add_defined(self, v):
            param = [self.data[0][x] + v.data[0][x]
                     for x in list(range(len(self)))]
            return self
        else:
            return None

    def __sub__(self: 'Vector', v: 'Vector') -> 'Vector' or None:
        if add_defined(self, v):
            param = [self.data[0][x] - v.data[0][x]
                     for x in range(len(self))]
            return Vector(param)
        else:
            return None

    def __mul__(self: 'Vector', c: Fraction) -> 'Vector':
        """
        :param c: is a number, pref and int
        :return: the product of a vector and a scalar
        """
        param = [c*x for x in self.data[0]]
        return Vector(param)

    def __rmul__(self: 'Vector', c: Fraction) -> 'Vector':
        return self*c

    def __eq__(self: 'Vector', v: 'Vector') -> bool:
        return self.data[0] == v.data[0]

    def __len__(self: 'Vector') -> int:
        return len(self.data[0])

def parallel(v1: 'Vector', v2: 'Vector') -> bool:
    """obj
    :param v: is a Vector
    :return: whether v is parallel to self
    """
    ratio = Fraction(v1.data[0][0], v2.data[0][0])
    v2 = ratio * v2
    return v1 == v2

def dot(self: 'Vector', v: 'Vector') -> int or None:
    """
    :param v: is a Vector obj
    :return: the dot product of self with v
    """
    result = int()
    # not: add_defined iff dot_defined
    if add_defined(self, v):
        return sum([self.data[0][x]+v.data[0][x]
                    for x in range(self.columns)])
    else:
        return None


# f: input -> bool
def add_defined(v1: 'Vector', v2: 'Vector') -> bool:
    return isinstance(v1, Vector) and isinstnace(v2, Vector) and\
        len(v1.data[0]) == len(v2.data[0])

def cross_defined(v1: Vector, v2: vector) -> bool:
    return isinstance(v1, Vector) and isinstance(v2, Vector)\
        and v1.length == v2.length == 3

# f: input -> Vector
def cross(v1: 'Vector', v2: 'Vector') -> Vector or None:
    """
    :param v: is a Vector obj
    :return: the cross product of self and v
    """
    if cross_defined(v1, v2):
        param = [v1.data[1]*v2.data[2]-v1.data[2]*v2.data[1],
                 v1.data[2]*v2.data[0]-v1.data[0]*v2.data[2],
                 v1.data[0]*v2.data[1]-v1.data[1]*v2.data[0]]
        return Vector(param)
    else:
        return None
