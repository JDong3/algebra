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
        elif isinstance(o, Matrix) and mul_defined(self, o):
            columns = col_vectors(o)
            for i in range(self.rows):
                param.append([list_dot(self.data[i], columns[x])
                              for x in range(o.columns)])
            return Matrix(param)
        # case: no sort of multiplication is defined
        else:
            return None

    def __rmul__(self: 'Matrix', x) -> 'Matrix':
        return self*x


# defined checker functions: they check if certain Matrix operations are
# defined or if the matrices satisfy certain properties
def add_defined(m1: 'Matrix', m2: 'Matrix') -> bool:
    return m1.rows == m2.rows and m1.columns == m2.columns


def mul_defined(m1: 'Matrix', m2: 'Matrix') -> bool:
    return m1.columns == m2.rows


def row_defined(m: 'Matrix', r: int) -> bool:
    return 0 <= r < m.rows


# helper matrix property functions: unofficial properties of mathematical
# matrices that are used to optimize computations
def col_vectors(m: 'Matrix') -> list:
    """
    :param m: is a matrix
    :return: a list of the column vectors of m 
    """
    columns = list()
    for i in range(m.columns):
        columns.append([m.data[x][i] for x in range(m.rows)])
    return columns


def pivot(m: 'Matrix', col: int) -> int or None:
    """
    :param m: is a matrix
    :param col: column that we want to find pivot of 
    :return: the row number of appropriate pivot
    """
    rows = m.data
    i = 0
    found = rows[i][col] != 0
    while not found:
        i += 1
        if rows[i][col] != 0:
            found = True
    return i if found else None


# matrix functions f: Matrix -> Number
def trace(m: 'Matrix') -> int:
    acc = int()
    for i in range(m.rows):
        acc += m.data[i][i]
    return acc


def anti_trace(m: 'Matrix') -> int:
    acc = int()
    for i in range(m.rows):
        acc += m.data[i][-(i+1)]
    return acc


def det(m: 'Matrix') -> int:
    """
    :return: the determinant of the m 
    """
    if m.rows == 1:
        result = m.data[0][0]
    elif m.rows == 2:
        result = trace(m) - anti_trace(m)
    else:
        result = int()
        for i in range(m.columns):
            result += cofactor(m, (1, i))
    return result


def cofactor(m: 'Matrix', index: tuple) -> int:
    """
    :param m: is a matrix
    :param index: is the index of the co-factor we want to compute 
    :return: the co-factor at index
    """
    param = list()
    for i in [x for x in list(range(m.rows)) if x != index[0]]:
        temp = list()
        for j in [x for x in list(range(m.columns)) if x != index[1]]:
            temp.append(m.data[i][j])
        param.append(temp)
    return int(math.pow(-1, index[0]+index[1])) + det(Matrix(param))


# matrix functions f: Matrix -> Matrix
def transpose(m: 'Matrix') -> 'Matrix':
    return Matrix(col_vectors(m))


def row_swap(m: 'Matrix', r1: int, r2: int) -> 'Matrix' or None:
    """
    :param m: is a matrix
    :param r1: is an int, 0 <= r1 < m.rows  
    :param r2: is ant int, 0 <= r2 < m.rows
    :return: a Matrix that is the result of the row swap of r1 and f2
    """
    param = copy.deepcopy(m.data)
    # check if r1 and f2 are in the bounds
    if row_defined(m, r1) and row_defined(m, r2):
        temp = param[r1]
        param[r1] = param[r2]
        param[r2] = temp
        return Matrix(param)
    else:
        return None


def row_add(m: 'Matrix', r1: int, r2: int, k: int=1):
    """
    :param m: is a matrix
    :param r1: 
    :param r2: 
    :param k: constant
    :return: a Matrix representation of the row operation adding r2 to r1
        ie. r1 -> r1 + r2
    """
    param = copy.deepcopy(m.data)
    param[r1] = [param[r1][x] + k*param[r2][x]
                 for x in range(m.columns)]
    return Matrix(param)


def row_scale(m: 'Matrix', r: int, k: int):
    param = copy.deepcopy(m.data)
    param[r] = [k*x for x in param[r]]
    return Matrix(param)


def rref(m: 'Matrix') -> 'Matrix':
    """
    :return: the Matrix representation of the Row Reduced Echelon Form m 
    """
    param = copy.deepcopy(m.data)
    m = Matrix(param)
    curr = 0
    for i in range(m.columns):
        # find an appropriate pivot
        p = pivot(m, i)
        # manipulate until pivot is 1 and pivotal column is empty
        m = m.row_swap(p, curr)
        m = m.row_scale(p, Fraction(1, m.val(p, i)))
        for j in range(curr, m.rows):
            m = m.row_add(j, p, -m.data[j][i])
        curr += 1
    return m
