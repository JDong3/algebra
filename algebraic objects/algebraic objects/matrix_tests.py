from matrix import *
import unittest


class ColVectorTests(unittest.TestCase):

    def test_single_element_case(self):
        self.assertEqual(col_vectors(Matrix([[1]])), [[1]])

    def test_matrix(self):
        self.assertEqual(
            col_vectors(Matrix([[1, 2, 3],
                                [1, 2, 3],
                                [1, 2, 3]])),
            [[1, 1, 1],
             [2, 2, 2],
             [3, 3, 3]])


class TransposeTests(unittest.TestCase):

    def test_single_element_case(self):
        self.assertEqual(transpose(Matrix([[1]])), Matrix([[1]]))

    def test_matrix(self):
        self.assertEqual(
            transpose(Matrix([[1, 1, 1],
                              [2, 2, 2],
                              [3, 3, 3]])),
            Matrix([[1, 2, 3],
                    [1, 2, 3],
                    [1, 2, 3]]))


class AddTests(unittest.TestCase):

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