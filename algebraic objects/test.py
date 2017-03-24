from functions import *
from calc import *
from vector import *
import unittest


class LCMTests(unittest.TestCase):
    def test_some_stuff(self):
        self.assertEqual(2, lcm(1, 2))
        self.assertEqual(9, lcm(3, 9))
        self.assertEqual(21, lcm(3,7))
        self.assertEqual(12, lcm(4, 6))


class VectorEqTests(unittest.TestCase):
    def test_some_stuff(self):
        self.assertEquals(Vector([1, 2, 3]),Vector([1, 2, 3]))
        self.assertNotEquals(Vector([1, 2, 3]), Vector([1, 3, 2]))


class VectorAddTests(unittest.TestCase):
    def test_some_stuff(self):
        self.assertEquals(Vector([2, 4, 6]),
                          Vector([1, 2, 3])+Vector([1, 2, 3]))


class VectorMulTests(unittest.TestCase):
    def test_some_stuff(self):
        self.assertEqual(Vector([2, 4, 6]), 2*Vector([1, 2, 3]))
        self.assertEqual(Vector([2, 4, 6]), Vector([1, 2, 3])*2)


class VectorParallelTests(unittest.TestCase):
    def test_some_stuff(self):
        self.assertTrue(parallel(Vector([1, 2, 3]), Vector([2, 4, 6])))
