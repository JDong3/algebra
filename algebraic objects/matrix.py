import copy
import math
from list_functions import *
from fractions import Fraction


class Matrix:
    """a class that represents a mathematical matrix"""
    def __init__(self: 'Matrix', data: list):
        # rep invar:
        # self.data represents the elements in the matrix
        # self.data is a twi dimensional list
        # the nth sublist of self.data is the nth row vector
        # the nth element in each of the sublists gives you the nth col vector
        self.data = data
        self.rows = len(data)
        self.columns = len(data[0])

    def __str__(self: 'Matrix') -> str:
        """
        :return: a string representation of a Matrix obj
        """
        # max_length_list is a list of the longest length elements in each
        # column of the matrix
        # we initialize the length of each of the elements in the first row of
        # our matrix to be the max_lengths
        max_length_list = [len(str(x)) for x in self.data[0]]
        result = str()
        # iterate through the rest of the rows in the matrix
        for row in range(1, self.rows):
            # and each of the columns in the rows
            for col in range(self.columns):
                # if we find an element in the matrix that is longer than the
                # current max_length element in that column
                if len(str(self.data[row][col])) > max_length_list[col]:
                    # the replace it with the new max_length
                    max_length_list[col] = len(str(self.data[row][col]))
        # to output a row of the matrix
        for row in range(self.rows):
            # start the line with a [
            result += '['
            for col in range(self.columns - 1):
                # at the string repr of each element of the row right
                # justifying the string to the max_length element of the column
                # spacing the elements of the row by two spaces
                result += str(self.data[row][col]).rjust(max_length_list[col])\
                          + '  '
            # same as above but for the last element of the row, there is no
            # need to add two spaces after it
            result += str(self.data[row][self.columns-1])\
                .rjust(max_length_list[self.columns-1])
            # end the row by adding a ] and a new line char
            result += ']' + '\n'
        return result

    def __eq__(self: 'Matrix', m: 'Matrix') -> bool:
        """
        If the .data .rows and .columns variables of two matrices are equal
        then, we say that the two matrices are equivalent or m1 == m2
        :param m: is a Matrix object
        :return: whether self and m are equivalent matrices
        """
        # isinstance is lazy evaluated first so we don't crash if we try to
        # compare a non matrix object to our matrix
        return isinstance(m, Matrix) and self.data == m.data and\
            self.rows == m.rows and self.columns == m.columns

    def __add__(self: 'Matrix', m: 'Matrix') -> 'Matrix' or None:
        """
        mathematical matrix addition
        :param m: is a Matrix obj
        :return: returns the sum of self and m
        """
        param = list()
        # case: matrix addition is defined
        if add_defined(self, m):
            # for each row in our matrix
            for i in range(self.rows):
                # create the resulting row after matrix addition is applied
                param.append([self.data[i][x] + m.data[i][x]
                              for x in range(self.columns)])
            return Matrix(param)
        # case: matrix addition is not defined
        else:
            return None

    def __mul__(self: 'Matrix', o: 'Matrix' or int) -> 'Matrix' or None:
        """
        mathematical matrix multiplication
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
        """
        :param x: is a constant
        :return: the product of a constant and a matrix
        """
        # this function will never trigger for matrix x matrix since it will
        # be caught by __mul__ first, unless you explicitly call
        # __rmul__ for some reason
        return self*x


# defined checker functions: they check if certain Matrix operations are
# defined or if the matrices satisfy certain properties
def add_defined(m1: 'Matrix', m2: 'Matrix') -> bool:
    """
    matrix addition is defined iff m1 and m2 are both matrices of the same
    dimension
    :param m1: is a matrix object
    :param m2: is a matrix object
    :return: whether the sum of m1 and m2 is defined
    """
    return isinstance(m1, Matrix) and isinstance(m2, Matrix) and\
        m1.rows == m2.rows and m1.columns == m2.columns


def mul_defined(m: 'Matrix' or Fraction, o: 'Matrix' or Fraction) -> bool:
    """
    matrix multiplication is defined for Matrix obj iff both m and o are\
    matrices or if m is a Matrix and o is a Fraction
    :param m: is a Matrix object
    :param o: is a Matrix or Fraction obj
    :return: whether the product of m and o is defined
    """
    # case: m and obj are matrices
    # not: lazy evaluation prevents crash if m or o is not Matrix obj
    if isinstance(m, Matrix) and isinstance(o, Matrix)\
       and m.columns == o.rows:
        return True
    # case: m is matrix and o is Fraction
    elif isinstance(m, Matrix) and isinstance(o, Fraction):
        return True
    # the case where m is Fraction and o is Matrix is caught by __rmul__ and
    # turned into the second case where m is matrix and o is Fraction
    else:
        return False


def row_defined(m: 'Matrix', r: int) -> bool:
    """
    a row r is said to be defined in a matrix m iff r corresponds to one of the
    row vectors of our matrix, in our case, this happens when r is in
    [0, .., m.rows-1]
    :param m: is a matrix object
    :param r: is an int
    :return: whether row r is defined for our matrix m
    """
    return 0 <= r < m.rows


def is_square(m: 'Matrix') -> bool:
    """
    a matrix is said to be square(nxn) if its number of columns is the same as
    the number of rows
    :param m: is a matrix object
    :return: whether m is a square matrix
    """
    return m.rows == m.columns


# helper matrix property functions: unofficial properties of mathematical
# matrices that are used to optimize computations
def col_vectors(m: 'Matrix') -> list:
    """
    gets a list two dimensional list that represents the column vectors of m,
    the list can be passed into a Matrix __init__ to construct the transpose
    of m
    :param m: is a matrix
    :return: a list representing the column vectors of m
    """
    columns = list()
    for i in range(m.columns):
        columns.append([m.data[x][i] for x in range(m.rows)])
    return columns


def pivot(m: 'Matrix', col: int, row: int=0) -> int or None:
    """
    find the first pivot in the col-th column of the matrix matrix starting
    from the row-th row
    :param m: is a matrix
    :param col: column that we want to find pivot of
    :param i: the start index of the search
    :return: the row number of appropriate pivot
    """
    # a row containing a non zero value in the row-th row and col-th column is
    # said to be a pivot that we are looking for
    found = False
    # while we are in bounds and have not yet found a pivot
    while row < len(m.data) and not found:
        if m.data[row][col] != 0:
            found = True
        row += 1
    return row-1 if found else None


# matrix functions f: Matrix -> Number
def trace(m: 'Matrix') -> Fraction:
    """
    the mathematical trace of the matrix or sum of the diagonal terms of the
    matrix m
    :param m: is a Matrix obj
    :return: the trace of m
    """
    return sum([m.data[x][x] for x in range(m.rows)])


def anti_trace(m: 'Matrix') -> Fraction:
    """
    we define the anti trace of the matrix m as the sum of the anti-diagonal
    terms of the matrix m
    :param m: is a nxn Matrix obj
    :return: the anti trace of m
    """
    return sum([m.data[x][-(x+1)] for x in range(m.rows)])


def mul_trace(m: 'Matrix') -> Fraction:
    """
    we define the multiplicative trace of the matrix m as the product of the
    diagonal terms of m
    :param m: is a nxn Matrix obj
    :return: the multiplicative trace of m
    """
    return list_prod([m.data[x][x] for x in range(m.rows)])


def mul_anti_trace(m: 'Matrix') -> Fraction:
    """
    we define the multiplicative anti trace of the matrix m as the product of
    the anti diagonal terms of m
    :param m: is a nxn Matrix obj
    :return: the multiplicative anti trace of m
    """
    return list_prod([m.data[x][-(x+1)] for x in range(m.rows)])


def det(m: 'Matrix') -> Fraction:
    """
    the mathematical determinant of the matrix
    :param m: is a nxn Matrix obj
    :return: the determinant of m
    """
    # idea first get the matrix into ref and record a 'k' that the det of the
    # matrix in ref form has to be mul by to get the det of the original matrix
    param = copy.deepcopy(m.data)
    m = Matrix(param)
    row = 0
    mul = 1
    for col in range(m.columns):
        piv = pivot(m, col, row)
        if piv is not None:
            if piv != row:
                m = row_swap(m, piv, row)
                mul = -mul
            for i in range(row+1, m.rows):
                    m = row_add(m, i, row,
                                -Fraction(m.data[i][col], m.data[row][col]))
        row += 1
    return mul*mul_trace(m)


def rec_det(m: 'Matrix') -> Fraction:
    """
    :param m: is a nxn matrix obj
    :return: the determinant of the m
    """
    if m.rows == 1:
        result = m.data[0][0]
    elif m.rows == 2:
        result = mul_trace(m) - mul_anti_trace(m)
    else:
        result = int()
        for i in range(m.columns):
            cof = cofactor(m, (0, i))
            result += m.data[0][i]*cofactor(m, (0, i))
    return result


def cofactor(m: 'Matrix', index: tuple) -> Fraction:
    """
    :param m: is a nxn matrix
    :param index: is the index of the co-factor we want to compute
    :return: the co-factor at index(signed determinant of a minor matrix)
    """
    return int(math.pow(-1, sum(index)))*det(minor(m, index))


# matrix functions f: Matrix -> Matrix
def transpose(m: 'Matrix') -> 'Matrix':
    """
    the transpose of a matrix m is a matrix s.t. each i,j th element of m is
    the j, i th element of transpose(m)
    :param m: is a matrix obj
    :return: the transpose of m
    """
    return Matrix(col_vectors(m))


def row_swap(m: 'Matrix', r1: int, r2: int) -> 'Matrix' or None:
    """
    elementary row operation, row swap r1 <-> r2
    :param m: is a matrix
    :param r1: is an int, 0 <= r1 < m.rows
    :param r2: is ant int, 0 <= r2 < m.rows
    :return: a Matrix that is the result of the row swap of r1 and r2
    """
    param = copy.deepcopy(m.data)
    # check if r1 and f2 are in the bounds
    if row_defined(m, r1) and row_defined(m, r2):
        # if so then swap r1 and r2
        temp = param[r1]
        param[r1] = param[r2]
        param[r2] = temp
        return Matrix(param)
    else:
        return None


def row_add(m: 'Matrix', r1: int, r2: int, k: Fraction=Fraction(1)):
    """
    elementary row operation, row addition r1 -> r1 + k*r2
    :param m: is a matrix
    :param r1: is an int, 0 <= r1 < m.rows
    :param r2: is an int, 0 <= r2 < m.rows
    :param k: is a Fraction obj
    :return: a Matrix representation of the row operation adding r2 to r1
        ie. r1 -> r1 + r2
    """
    param = copy.deepcopy(m.data)
    param[r1] = [param[r1][x] + k*param[r2][x]
                 for x in range(m.columns)]
    return Matrix(param)


def row_scale(m: 'Matrix', r: int, k: Fraction=Fraction(1)):
    """
    elementary row operation, row multiplication by scalar constant r1 -> k*r1
    :param m: is a matrix
    :param r: is an int, 0 <= r < m.rows
    :param k: is a Fraction obj
    :return:
    """
    param = copy.deepcopy(m.data)
    param[r] = [k*x for x in param[r]]
    return Matrix(param)


def rref(m: 'Matrix') -> 'Matrix':
    """
    :return: the Matrix representation of the Row Reduced Echelon Form m
    """
    param = copy.deepcopy(m.data)
    m = Matrix(param)
    # toggle print(m)
    row = 0
    # for each column in m.data
    for col in range(m.columns):
        # try to find a pivot for that column
        piv = pivot(m, col, row)
        # if a pivot is found
        if piv is not None:
            # manipulate until pivot is 1 and pivotal column is empty
            m = row_swap(m, piv, row)
            # toggle print(m)
            m = row_scale(m, piv, Fraction(1, m.data[piv][col]))
            # toggle print(m)
            for j in range(m.rows):
                if j != row:
                    m = row_add(m, j, row, -m.data[j][col])
                    # toggle print(m)
        row += 1
    return m


def minor(m: 'Matrix', index: tuple) -> 'Matrix':
    """
    :param m: is a matrix
    :tuple index: is the index of the ith row and jth column that will be
        removed
    :return: a minor matrix of m without the ith and jth rows and columns
    """
    param = list()
    for k in range(m.rows):
        if k != index[0]:
            param.append([m.data[k][x] for x in range(m.columns) if x != index[1]])
    return Matrix(param)


def adjugate(m: 'Matrix') -> 'Matrix':
    """
    the mathematical adjugate of m
    :param m: is a nxn matrix matrix
    :return: the adjugate of m
    """
    # idea: first construct the cofactor matrix, then transpose it
    param = list()
    if is_square(m):
        for row in m.rows:
            param.append([cofactor(m, (row, x)) for x in range(m.columns)])
        return Matrix(param)
    else:
        return None


def inverse(m: 'Matrix') -> 'Matrix':
    """
    :param m: is a nxn matrix
    :return: the inverse matrix of m
    """
    # inefficient method: first look for det of m, if its 0 then there is no
    # inverse, otherwise compute the inverse
    if det(m) != 0:
        return Fraction(1, det(m))*transpose(adjugate(m))
    else:
        return None


if __name__ == '__main__':
    rref(Matrix([[19, 25, 21, 10],
                 [74, 61, 77, 79],
                 [66, 88, 3, 39],
                 [90, 99, 69, 32]]))
    help(Matrix)

    det(Matrix([[3, 2, 1],
                [0, 2, 1],
                [0, 0, -2]]))
