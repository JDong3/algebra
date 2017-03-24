"""representing vectors from a functional perspective"""
from matrix import Matrix
import calc


class Vector(Matrix):
    """a class that represents a mathematical vector"""
    def __init__(self: 'Vector', data: list) -> None:
        Matrix.__init__(self, [data])
        
    
    def __str__(self: 'Vector') -> str:
        return str(self.data[0])

    def __add__(self: 'Vector', v: 'Vector') -> 'Vector':
        """
        :param v: is a vector object
        :return: the sum of self and another vector object
        """
        len1, len2, = len(self.data[0]), len(v.data[0])
        param = list()
        if self.similar(v):
            for i in range(len1):
                param.append(self.data[0][i] + v.data[0][i])
        else:
            data = None
        return Vector(param)

    def __mul__(self: 'Vector', c: int) -> 'Vector':
        """
        :param c: is a number, pref and int
        :return: the product of a vector and a scalar
        """
        param = list()
        for i in range(len(self.data[0])):
            param.append(c*self.data[0][i])
        return Vector(param)

    def __rmul__(self: 'Vector', c: int) -> 'Vector':
        return self*c

    def __eq__(self: 'Vector', v: 'Vector') -> bool:
        result = True
        if self.similar(v):
            for i in range(len(self.data[0])):
                if self.data[0][i] != v.data[0][i]:
                    result = False
        else:
            result = False
        return result

    def parallel(self: 'Vector', v: 'Vector') -> bool:
        """
        :param v: is a Vector obj
        :return: whether v is parallel to self
        """
        # find the LCM
        l = calc.lcm(1, 2)
        # find out what to multiply each vector by to make the scalar on the
        # first dimension of the vectors equal
        c1 = l/self.data[0][0]
        c2 = l/v.data[0][0]
        self_prime = c1*self
        v_prime = c2*v
        return self_prime == v_prime

    def dot(self: 'Vector', v: 'Vector') -> int:
        """
        :param v: is a Vector obj
        :return: the dot product of self with v
        """
        result = int()
        if self.similar(v):
            for i in range(len(self.data[0])):
                result += self.data[0][i]*v.data[0][i]
        else:
            result = None
        return result

    def similar(self: 'Vector', v: 'Vector') -> bool:
        return len(self.data[0]) == len(v.data[0])

    def cross(self: 'Vector', v: 'Vector') -> 'Vector':
        """
        :param v: is a Vector obj 
        :return: the cross product of self and v
        """
        # implement with matrix multiplication

        self_mod, v_mod = list(), list()
        # construct self_mod
        self_mod = [[0, -self.data[0][2], self.data[0][1]],
                    [self.data[0][2]], 0, -self.data[0][0],
                    [-self.data[0][1]], self.data[0][0], 0]
        v_mod = [[v.data[0][0]], [v.data[0][1]], v.data[0][2]]

def parallel(v1: 'Vector', v2: 'Vector') -> bool:
    return v1.parallel(v2)


def dot(v1: 'Vector', v2: 'Vector') -> int:
    return v1.dot(v2)


def similar(v1: 'Vector', v2: 'Vector') -> bool:
    return v1.similar(v2)


def cross(v1: 'Vector', v2: 'Vector') -> 'Vector':
    pass