from vector import *
import unittest


class VectorEqTests(unittest.TestCase):
    def test_some_stuff(self):
        self.assertEquals(Vector([1, 2, 3]),Vector([1, 2, 3]))
        self.assertNotEquals(Vector([1, 2, 3]), Vector([1, 3, 2]))


class VectorAddTests(unittest.TestCase):
    def test_some_stuff(self):
        self.assertEquals(Vector([2, 4, 6]),
                          Vector([1, 2, 3])+Vector([1, 2, 3]))


class VectorMulTests(unittest.TestCase):
    def test_positive_const_mul(self):
        self.assertEqual(Vector([2, 4, 6]), 2*Vector([1, 2, 3]))
        self.assertEqual(Vector([2, 4, 6]), Vector([1, 2, 3])*2)

    def test_negative_const_mul(self):
        self.assertEqual(Vector([-2, -4, -6]), -2*Vector([1, 2, 3]))
        self.assertEqual(Vector([-2, -4, -6]), Vector([1, 2, 3])*-2)


class VectorParallelTests(unittest.TestCase):
    def test_some_stuff(self):
        self.assertTrue(parallel(Vector([1, 2, 3]), Vector([2, 4, 6])))
        self.assertTrue(parallel(Vector([1, 2, 3]), Vector([-1, -2, -3])))


class VectorDotTests(unittest.TestCase):
    def test_some_stuff(self):
        self.assertEqual(dot(Vector([1, 2, 3]), Vector([1, 2, 3])), 14)
        self.assertEqual(dot(Vector([1, 0]), Vector([0, 1])), 0)

unittest.main()
