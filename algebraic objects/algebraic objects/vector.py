"""representing vectors from a functional perspective"""
from matrix import Matrix
from fractions import Fraction
import copy
'''
restructuring Vector
algorithms with Fraction object
implementation of data[0]
'''


class Vector(Matrix):
    """a class that represents a mathematical vector"""
    def __init__(self: 'Vector', data: list) -> None:
        Matrix.__init__(self, [data])

    def __str__(self: 'Vector') -> str:
        return str(self.data[0])

    def __add__(self: 'Vector', v: 'Vector') -> 'Vector' or None:
        """
        :param v: is a vector object
        :return: the sum of self and another vector object
        """
        if self.same_size(v):
            self.data[0] = [self.data[0][x] + v.data[0][x]
                     for x in list(range(len(self)))]
            return self
        else:
            return None  # suspect line

    def __sub__(self: 'Vector', v: 'Vector') -> 'Vector' or None:
        if self.same_size(v):
            param = [self.data[0][x] - v.data[0][x]
                     for x in range(len(self))]
            return Vector(param)
        else:
            return None

    def __mul__(self: 'Vector', c: int) -> 'Vector':
        """
        :param c: is a number, pref and int
        :return: the product of a vector and a scalar
        """
        param = [c*x for x in self.data[0]]
        return Vector(param)

    def __rmul__(self: 'Vector', c: int) -> 'Vector':
        return self*c

    def __eq__(self: 'Vector', v: 'Vector') -> bool:
        return self.data[0] == v.data[0]

    def __len__(self: 'Vector') -> int:
        return len(self.data[0])

    def parallel(self: 'Vector', v: 'Vector') -> bool:
        """obj
        :param v: is a Vector 
        :return: whether v is parallel to self
        """
        ratio = Fraction(self.data[0][0], v.data[0][0])
        v = ratio * v
        result = True
        for i in range(len(self.data[0])):
            if self.data[0][i] != v.data[0][i]:
                result = False
        return result

    def dot(self: 'Vector', v: 'Vector') -> int or None:
        """
        :param v: is a Vector obj
        :return: the dot product of self with v
        """
        result = int()
        if self.same_size(v):
            return sum([self.data[0][x]+v.data[0][x]\
                        for x in range(self.columns)])
        else:
            return None

    def same_size(self: 'Vector', v: 'Vector') -> bool:
        return len(self.data[0]) == len(v.data[0])

    def cross(self: 'Vector', v: 'Vector') -> Matrix:
        """
        :param v: is a Vector obj 
        :return: the cross product of self and v
        """
        # implement with matrix multiplication

        self_mod, v_mod = list(), list()
        # construct self_mod
        self_mod = Matrix([[0, -self.data[0][2], self.data[0][1]],
                           [self.data[0][2], 0, -self.data[0][0]],
                           [-self.data[0][1], self.data[0][0], 0]])
        v_mod = Matrix([[v.data[0][0]], [v.data[0][1]], v.data[0][2]])
        return self_mod*v_mod
