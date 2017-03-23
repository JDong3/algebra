"""representing vectors from a functional perspective"""


class Matrix():
    """a class that represents a mathematical matrix"""
    def __init__(self: 'Vector', data: list):
        self.data = data


class Vector(Matrix):
    """a class that represents a mathematical vector"""
    def __init__(self: 'Vector', data: list):
        Matrix.__init__(self, data)

    def sum(self: 'Matrix', m: 'Matrix'):
        """
        :param m: is a vector object
        :return: the sum of self and another vector object
        """
        len1, len2, = len(self.data), len(m.data)
        param = list()
        if len1 == len2:
            for i in range(len1):
                param.append(self.data[i] + m.data[i])
        else:
            data = None
        return Vector(param)

    def product(self, c: int):
        """
        :param i: is a number, pref and int
        :return: the product of a vector and a scalar
        """
        param = list()
        for i in range(len(self.data)):
            param.append(c*self.data[i])
        return Vector(param)


def sum(m1: 'Matrix', m2: 'Matrix') -> 'Matrix':
    """
    addition defined for algebraic objects
    :param m1: is a Matrix obj
    :param m2: is a Matrix obj
    :return: the sum of m1 and m2
    """
    return m1.sum(m2)


def product(m: 'Matrix', c: int) -> 'Matrix':
    """
    scalar multiplication defined for algebraic objects
    :param m: is a Matrix obj
    :param c: is a number, pref an int
    :return: the product of m and c
    """
    return m.product(c)