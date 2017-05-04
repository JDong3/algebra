from matrix import *
import unittest


class ColVectorTests(unittest.TestCase):

    def test_single_element_case(self):
        self.assertEqual(col_vectors(Matrix([[1]])), [[1]])

    def test_multiple_element_matrix(self):
        self.assertEqual(
            col_vectors(Matrix([[1, 2, 3],
                                [1, 2, 3],
                                [1, 2, 3]])),
            [[1, 1, 1],
             [2, 2, 2],
             [3, 3, 3]])
        # a 3x4 matrix
        self.assertEqual(col_vectors(Matrix([[1, 2, 3, 4],
                                             [1, 2, 3, 4],
                                             [1, 2, 3, 4]])),
                         [[1, 1, 1],
                          [2, 2, 2],
                          [3, 3, 3],
                          [4, 4, 4]])

    def test_column_vector(self):
        self.assertEqual(col_vectors(Matrix([[1],
                                             [2],
                                             [3],
                                             [4],
                                             [5]])), [[1, 2, 3, 4, 5]])

    def test_row_vector(self):
        self.assertEqual(col_vectors(Matrix([[1, 2, 3, 4, 5]])),
                         [[1],
                          [2],
                          [3],
                          [4],
                          [5]])


class TransposeTests(unittest.TestCase):

    def test_single_element_case(self):
        self.assertEqual(transpose(Matrix([[1]])), Matrix([[1]]))

    def test_multiple_element_matrix(self):
        self.assertEqual(transpose(Matrix([[1, 2, 3],
                                           [1, 2, 3],
                                           [1, 2, 3]])),
                         Matrix([[1, 1, 1],
                                 [2, 2, 2],
                                 [3, 3, 3]]))
        # a 3x4 matrix
        self.assertEqual(transpose(Matrix([[1, 2, 3, 4],
                                           [1, 2, 3, 4],
                                           [1, 2, 3, 4]])),
                         Matrix([[1, 1, 1],
                                 [2, 2, 2],
                                 [3, 3, 3],
                                 [4, 4, 4]]))

    def test_column_vector(self):
        self.assertEqual(transpose(Matrix([[1],
                                           [2],
                                           [3],
                                           [4],
                                           [5]])),
                         Matrix([[1, 2, 3, 4, 5]]))

    def test_row_vector(self):
        self.assertEqual(transpose(Matrix([[1, 2, 3, 4, 5]])),
                         Matrix([[1],
                                 [2],
                                 [3],
                                 [4],
                                 [5]]))


class AddTests(unittest.TestCase):

    def test_single_element_case(self):
        self.assertEqual(Matrix([[1, 2, 3, 4]])+
                         Matrix([[1, 2, 3, 4]]),
                         Matrix([[2, 4, 6, 8]]))

    def test_stuff(self):
        self.assertEqual(Matrix([[1, 2, 3],
                                 [1, 2, 3],
                                 [1, 2, 3]]) +
                         Matrix([[1, 2, 3],
                                 [1, 2, 3],
                                 [1, 2, 3]]),
                         Matrix([[2, 4, 6],
                                 [2, 4, 6],
                                 [2, 4, 6]]))


class RowSwapTests(unittest.TestCase):

    def test_stuff(self):
        self.assertEqual(row_swap(Matrix([[1, 1, 1],
                                          [2, 2, 2],
                                          [3, 3, 3]]), 0, 1),
                         Matrix([[2, 2, 2],
                                 [1, 1, 1],
                                 [3, 3, 3]]))
        self.assertEqual(row_swap(Matrix([[1, 1, 1],
                                          [2, 2, 2],
                                          [3, 3, 3]]), 0, 2),
                         Matrix([[3, 3, 3],
                                 [2, 2, 2],
                                 [1, 1, 1]]))
        self.assertEqual(row_swap(Matrix([[1, 1, 1],
                                          [2, 2, 2],
                                          [3, 3, 3]]), 2, 1),
                         Matrix([[1, 1, 1],
                                 [3, 3, 3],
                                 [2, 2, 2]]))


class RowAddTests(unittest.TestCase):
    def test_stuff(self):
        self.assertEqual(row_add(Matrix([[1, 0, 0],
                                        [0, 1, 0],
                                        [0, 0, 1]]), 0, 1, 3),
                         Matrix([[1, 3, 0],
                                 [0, 1, 0],
                                 [0, 0, 1]]))
        self.assertEqual(row_add(Matrix([[1, 0, 0],
                                         [0, 1, 0],
                                         [0, 0, 1]]), 0, 1, -Fraction(5,2)),
                         Matrix([[1, -Fraction(5,2), 0],
                                 [0, 1, 0],
                                 [0, 0, 1]]))


class RowScaleTests(unittest.TestCase):
    def test_stuff(self):
        self.assertEqual(row_scale(Matrix([[1, 2, 3],
                                           [1, 2, 3],
                                           [1, 2, 3]]), 2, 3),
                         Matrix([[1, 2, 3],
                                 [1, 2, 3],
                                 [3, 6, 9]]))
        self.assertEqual(row_scale(Matrix([[1, 2, 3],
                                           [1, 2, 3],
                                           [1, 2, 3]]), 2, -Fraction(1, 5)),
                         Matrix([[1, 2, 3],
                                 [1, 2, 3],
                                 [-Fraction(1, 5), -Fraction(2, 5), -Fraction(3, 5)]]))


class RrefTests(unittest.TestCase):
    def test_stuff(self):
        self.assertEqual(rref(Matrix([[3, 0, 0],
                                      [0, 3, 0],
                                      [0, 0, 3]])),
                         Matrix([[1, 0, 0],
                                 [0, 1, 0],
                                 [0, 0, 1]]))
        self.assertEqual(rref(Matrix([[3, 3, 3],
                                      [3, 3, 3],
                                      [3, 3, 3]])),
                         Matrix([[1, 1, 1],
                                 [0, 0, 0],
                                 [0, 0, 0]]))


class MinorTests(unittest.TestCase):
    def test_stuff(self):
        m = Matrix([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
        self.assertEqual(minor(Matrix([[1, 2, 3],
                                      [4, 5, 6],
                                      [7, 8, 9]]), (0, 0)),
                         Matrix([[5, 6],
                                 [8, 9]]))
        self.assertEqual(minor(Matrix([[1, 2, 3],
                                       [4, 5, 6],
                                       [7, 8, 9]]), (0, 1)),
                         Matrix([[4, 6],
                                 [7, 9]]))
        self.assertEqual(minor(Matrix([[1, 2, 3],
                                       [4, 5, 6],
                                       [7, 8, 9]]), (0, 2)),
                         Matrix([[4, 5],
                                 [7, 8]]))
        self.assertEqual(minor(Matrix([[1, 2, 3],
                                       [4, 5, 6],
                                       [7, 8, 9]]), (1, 0)),
                         Matrix([[2, 3],
                                 [8, 9]]))
        self.assertEqual(minor(Matrix([[1, 2, 3],
                                       [4, 5, 6],
                                       [7, 8, 9]]), (1, 1)),
                         Matrix([[1, 3],
                                 [7, 9]]))
        self.assertEqual(minor(Matrix([[1, 2, 3],
                                       [4, 5, 6],
                                       [7, 8, 9]]), (1, 2)),
                         Matrix([[1, 2],
                                 [7, 8]]))
        self.assertEqual(minor(Matrix([[1, 2, 3],
                                       [4, 5, 6],
                                       [7, 8, 9]]), (2, 0)),
                         Matrix([[2, 3],
                                 [5, 6]]))
        self.assertEqual(minor(Matrix([[1, 2, 3],
                                       [4, 5, 6],
                                       [7, 8, 9]]), (2, 1)),
                         Matrix([[1, 3],
                                 [4, 6]]))
        self.assertEqual(minor(Matrix([[1, 2, 3],
                                       [4, 5, 6],
                                       [7, 8, 9]]), (2, 2)),
                         Matrix([[1, 2],
                                 [4, 5]]))


class TraceTests(unittest.TestCase):
    def test_stuff(self):
        m = Matrix([[2, 0, 0],
                    [0, 3, 0],
                    [0, 0, 7]])
        self.assertEqual(trace(Matrix([[2, 0, 0],
                                       [0, 3, 0],
                                       [0, 0, 7]])), 12)
        self.assertEqual(trace(Matrix([[2, -3, 2],
                                       [3, 3, 6],
                                       [4, 6, 7]])), 12)
        self.assertEqual(trace(Matrix([[-2, 0, 0],
                                       [0, 3, 0],
                                       [0, 0, 7]])), 8)


class AntiTraceTests(unittest.TestCase):
    def test_stuff(self):
        m = Matrix([[0, 0, 2],
                    [0, 3, 0],
                    [7, 0, 0]])
        self.assertEqual(anti_trace(Matrix([[0, 0, 2],
                                            [0, 3, 0],
                                            [7, 0, 0]])), 12)
        self.assertEqual(anti_trace(Matrix([[3, 3, 2],
                                            [3, 3, 3],
                                            [7, 3, 3]])), 12)
        self.assertEqual(anti_trace(Matrix([[0, 0, -2],
                                            [0, 3, 0],
                                            [7, 0, 0]])), 8)


class MulTraceTests(unittest.TestCase):
    def test_stuff(self):
        m = Matrix([[2, 0, 0],
                    [0, 3, 0],
                    [0, 0, 7]])
        self.assertEqual(mul_trace(Matrix([[2, 0, 0],
                                           [0, 3, 0],
                                           [0, 0, 7]])), 42)
        self.assertEqual(mul_trace(Matrix([[2, -3, 2],
                                           [3, 3, 6],
                                           [4, 6, 7]])), 42)
        self.assertEqual(mul_trace(Matrix([[-2, 0, 0],
                                           [0, 3, 0],
                                           [0, 0, 7]])), -42)


class MulAntiTraceTests(unittest.TestCase):
    def test_stuff(self):
        m = Matrix([[0, 0, 2],
                    [0, 3, 0],
                    [7, 0, 0]])
        self.assertEqual(mul_anti_trace(Matrix([[0, 0, 2],
                                                [0, 3, 0],
                                                [7, 0, 0]])), 42)
        self.assertEqual(mul_anti_trace(Matrix([[3, 3, 2],
                                                [3, 3, 3],
                                                [7, 3, 3]])), 42)
        self.assertEqual(mul_anti_trace(Matrix([[0, 0, -2],
                                                [0, 3, 0],
                                                [7, 0, 0]])), -42)


class RecDetTests(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(rec_det(Matrix([[5]])), 5)

    def test_2x2_matrix(self):
        self.assertEqual(rec_det(Matrix([[1, 0],
                                         [0, 1]])), 1)
        self.assertEqual(rec_det(Matrix([[1, 1],
                                         [1, 1]])), 0)
        self.assertEqual(rec_det(Matrix([[2, 5],
                                         [7, 3]])), -29)

    def test_3x3_matrix(self):
        self.assertEqual(rec_det(Matrix([[3, 2, 1],
                                         [0, 2, 1],
                                         [0, 0, -2]])), -12)


class DetTests(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(det(Matrix([[5]])), 5)

    def test_2x2_matrix(self):
        self.assertEqual(det(Matrix([[1, 0],
                                     [0, 1]])), 1)
        self.assertEqual(det(Matrix([[1, 1],
                                     [1, 1]])), 0)
        self.assertEqual(det(Matrix([[2, 5],
                                     [7, 3]])), -29)

    def test_3x3_matrix(self):
        self.assertEqual(det(Matrix([[3, 2, 1],
                                     [0, 2, 1],
                                     [0, 0, -2]])), -12)

unittest.main()
