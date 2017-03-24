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

    def __rmul__(self: 'Matrix', x) -> 'Matrix':
        return self*x

    def similar(self: 'Matrix', m: 'Matrix'):
        return self.rows == m.rows and self.columns == m.columns

    def matrix_mul_defined(self: 'Matrix', m: 'Matrix'):
        return self.columns == m.rows
