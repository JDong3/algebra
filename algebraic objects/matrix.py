import copy
from vector import Vector


class Matrix():
    """a class that represents a mathematical matrix"""
    def __init__(self: 'Matrix', data: list):
        self.data = data
        self.rows = len(data)
        self.columns = len(data[0])

    def col_vectors(self: 'Matrix') -> list:
        """
        :return: a list of the column vectors of self 
        """
        column_vectors = list()
        # for each index of a row vector
        for i in range(self.rows):
            column_vector = list()
            # iterate through each list in data
            for j in range(self.columns):
                column_vector.append(self.data[j][i])
            column_vectors.append(column_vector)
        return column_vectors

    def __str__(self):
        """
        :return: a string representation of a Matrix obj 
        """
        result = str()
        for i in range(self.rows):
            result += ' ' + self.data[i].__str__() + '\n'
        return result

    def __add__(self: 'Matrix', m: 'Matrix') -> 'Matrix' or None:
        """
        :param m: is a Matrix obj 
        :return: returns the sum of self and m
        """
        param = list()
        if self.similar(m):
            for i in range(self.rows):
                row = list()
                for j in range(self.columns):
                    row.append(self.data[i][j] + m.data[i][j])
                param.append(row)
            result = Matrix(param)
        else:
            result = None
        return result

    def __mul__(self: 'Matrix', x) -> 'Matrix':
        """
        :param x: is a constant or a Matrix obj 
        :return: the product of self and x
        """
        param = list()
        if isinstance(x, int):
            for i in range(self.rows):
                row = list()
                for j in range(self.columns):
                    row.append(x*self.data[i][j])
                param.append(row)
            result = Matrix(param)
        elif isinstance(x, Matrix) and self.matrix_mul_defined(x):
            for i in range(self.rows):
                row = list()
                for j in range(self.columns):
                    row.append(self.data[i][j]*x.data[i][j])
            result = Matrix(param)
        else:
            result = None
        return result

    def transpose(self: 'Matrix') -> 'Matrix':
        """
        :return: the Matrix representation of the transpose of self 
        """
        # if you input the column vectors of self into
        param = self.col_vectors()
        return Matrix(param)

    def rref(self: 'Matrix') -> 'Matrix':
        """
        :return: the Matrix representation of the Row Reduced Echelon Form self 
        """
        pass

    def row_swap(self: 'Matrix', r1: int, r2: int) -> 'Matrix':
        """
        :param r1: is an int, 0 <= r1 < self.rows  
        :param r2: is ant int, 0 <= r2 < self.rows
        :return: a Matrix that is the result of the row swap of r1 and f2
        """
        param = copy.deepcopy(self.data)
        # check if r1 and f2 are in the bounds
        if self.legal_row(r1) and self.legal_row(r2):
            temp = param[r1]
            param[r1] = param[r2]
            param[r2] = temp
            result = Matrix(param)
        else:
            result = None
        return result

    def row_add(self, r1: int, r2: int):
        """
        :param r1: 
        :param r2: 
        :return: a Matrix representation of the row operation adding r2 to r1
            ie. r1 -> r1 + r2
        """
        param = copy.deepcopy(self.data)
        if self.legal_row(r1) and self.legal_row(r2):
            v1, v2 = Vector(param[r1]), Vector(param[r2])
            v3 = v1 + v2
            param[r1] = v3.data[0]
            result = Matrix(param)


    def __rmul__(self: 'Matrix', x) -> 'Matrix':
        return self*x

    def legal_row(self: 'Matrix', r: int) -> bool:
        return 0 <= r < self.columns

    def similar(self: 'Matrix', m: 'Matrix'):
        return self.rows == m.rows and self.columns == m.columns

    def matrix_mul_defined(self: 'Matrix', m: 'Matrix') -> bool:
        return self.columns == m.rows
