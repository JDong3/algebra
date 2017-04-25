import copy
import math
from list_functions import *
from fractions import Fraction


class Matrix:
    """a class that represents a mathematical matrix"""
    def __init__(self: 'Matrix', data: list):
        # on the fly fraction object injection
        self.data = data
        self.rows = len(data)
        self.columns = len(data[0])

    def __str__(self):
        """
        :return: a string representation of a Matrix obj 
        """
        result = str()
        for i in range(self.rows):
            result += ' ' + self.data[i].__str__() + '\n'
        return result

    def __eq__(self: 'Matrix', m: 'Matrix') -> bool:
        return self.data == m.data and self.rows == m.rows and\
            self.columns == m.columns

    def __add__(self: 'Matrix', m: 'Matrix') -> 'Matrix' or None:
        """
        :param m: is a Matrix obj 
        :return: returns the sum of self and m
        """
        param = list()
        # case: matrix addition is defined
        if add_defined(self, m):
            # implement matrix addition
            for i in range(self.rows):
                param.append([self.data[i][x] + m.data[i][x]
                              for x in range(self.columns)])
            return Matrix(param)
        # case: matrix addition is not defined
        else:
            return None

    def __mul__(self: 'Matrix', o: 'Matrix' or int) -> 'Matrix' or None:
        """
        :param o: is a constant or a Matrix obj 
        :return: the product of self and o
        """
        param = list()
        # case: scalar multiplication of matrix is always defined
        if isinstance(o, int):
            for i in range(self.rows):
                param.append([o*x for x in self.data[i]])
            return Matrix(param)
        # case: transform of a matrix on a matrix is defined
        # note check for instance of matrix first or risk a crash
        elif isinstance(o, Matrix) and self.matrix_mul_defined(o):
            columns = col_vectors(o)
            for i in range(self.rows):
                param.append([list_dot(self.data[i], columns[x])
                              for x in range(o.columns)])
            return Matrix(param)
        # case: no sort of multiplication is defined
        else:
            return None

    def rref(self: 'Matrix') -> 'Matrix':
        """
        :return: the Matrix representation of the Row Reduced Echelon Form self 
        """
        param = copy.deepcopy(self.data)
        m = Matrix(param)
        curr = 0
        for i in range(self.columns):
            # find an appropriate pivot
            p = self.pivot(i)
            # manipulate until pivot is 1 and pivotal column is empty
            m = m.row_swap(p, curr)
            m = m.row_scale(p, Fraction(1, m.val(p, i)))
            for j in range(curr, self.rows):
                m = m.row_add(j, p, -self.val(j, i))
            curr += 1
        return m

    def pivot(self: 'Matrix', col: int) -> int or None:
        """
        :param col: column that we want to find pivot of 
        :return: the row number of appropriate pivot
        """
        rows = self.data
        i = 0
        found = rows[i][col] != 0
        while not found:
            i += 1
            if rows[i][col] != 0:
                found = True
        return i if found else None

    def row_swap(self: 'Matrix', r1: int, r2: int) -> 'Matrix' or None:
        """
        :param r1: is an int, 0 <= r1 < self.rows  
        :param r2: is ant int, 0 <= r2 < self.rows
        :return: a Matrix that is the result of the row swap of r1 and f2
        """
        param = copy.deepcopy(self.data)
        # check if r1 and f2 are in the bounds
        if self.row_defined(r1) and self.row_defined(r2):
            temp = param[r1]
            param[r1] = param[r2]
            param[r2] = temp
            return Matrix(param)
        else:
            return None

    def row_add(self, r1: int, r2: int, k: int=1):
        """
        :param r1: 
        :param r2: 
        :param k: constant
        :return: a Matrix representation of the row operation adding r2 to r1
            ie. r1 -> r1 + r2
        """
        param = copy.deepcopy(self.data)
        param[r1] = [param[r1][x] + k*param[r2][x]
                     for x in range(self.columns)]
        return Matrix(param)

    def row_scale(self, r: int, k: int):
        param = copy.deepcopy(self.data)
        param[r] = [k*x for x in param[r]]
        return Matrix(param)

    def val(self: 'Matrix', i: int, j: int) -> int:
        return self.data[i][j]

    def det(self: 'Matrix') -> int:
        """
        :return: the determinant of the self 
        """
        if self.rows == 1:
            result = self.data[0][0]
        elif self.rows == 2:
            result = self.trace() - self.anti_trace()
        else:
            result = int()
            for i in range(self.columns):
                result += self.cofactor((1, i))
        return result

    def cofactor(self: 'Matrix', index: tuple) -> int:
        """
        :param index: is the index of the co-factor we want to compute 
        :return: the co-factor at index
        """
        param = list()
        for i in [x for x in list(range(self.rows)) if x != index[0]]:
            temp = list()
            for j in [x for x in list(range(self.columns)) if x != index[1]]:
                temp.append(self.data[i][j])
            param.append(temp)
        return int(math.pow(-1, index[0]+index[1])) + Matrix(param).det()

    def trace(self: 'Matrix') -> int:
        """
        :return: the trace of self 
        """
        acc = int()
        for i in range(self.rows):
            acc += self.data[i][i]
        return acc

    def anti_trace(self: 'Matrix') -> int:
        """
        :return: return the anti trace of self (the sum of the anti-diagonals) 
        """
        acc = int()
        for i in range(self.rows):
            acc += self.data[i][-(i+1)]
        return acc

    def __rmul__(self: 'Matrix', x) -> 'Matrix':
        return self*x

    def row_defined(self: 'Matrix', r: int) -> bool:
        return 0 <= r < self.columns

    def similar(self: 'Matrix', m: 'Matrix'):
        return self.rows == m.rows and self.columns == m.columns

    def matrix_mul_defined(self: 'Matrix', m: 'Matrix') -> bool:
        return self.columns == m.rows


# defined checker functions: they check if certain Matrix operations are
# defined
def add_defined(m1: 'Matrix', m2: 'Matrix') -> bool:
    return m1.rows == m2.rows and m1.columns == m2.columns


def mul_defined(m1: 'Matrix', m2: 'Matrix') -> bool:
    return m1.columns == m2.rows


# helper matrix property functions: unofficial properties of mathematical
# matrices that are used to optimize computations
def col_vectors(m: 'Matrix') -> list:
    """
    :return: a list of the column vectors of self 
    """
    columns = list()
    for i in range(m.columns):
        columns.append([m.data[x][i] for x in range(m.rows)])
    return columns


# matrix property functions: recognized properties of mathematical matricies
def transpose(m: 'Matrix') -> 'Matrix':
    return Matrix(col_vectors(m))
