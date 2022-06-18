import unittest

from multi_example import *


class TestMultimethod(unittest.TestCase):

    # 1.Run different functions for different types
    def test_type(self):
        self.assertEqual(example_function(1, 1), 2)
        self.assertEqual(example_function(1.0, 1.0), 0.0)
        self.assertEqual(example_function('he', 'llo'), 'hello')
        self.assertEqual(example_function('1', 10), '110')

    # 2.Optional and named parameters
    def test_optional(self):
        self.assertEqual(example_function('1'), '110')
        self.assertEqual(example_function('1', 9), '19')

        self.assertEqual(example_function(1.0, 9, 10), 20)
        self.assertEqual(example_function(1.0), 21.0)
        self.assertEqual(example_function(1.0, 9), 20)

    # 3.support for named argumants
    def test_named_object(self):
        self.assertEqual(example_function(a=1, b=2), 3)
        self.assertEqual(example_function(a='1', b=10), '110')

    # 4.inherit
    def test_inherit(self):
        self.assertEqual(example_function(A(), A()), 'works')
        self.assertEqual(example_function(A(), B()), 'works')
        self.assertEqual(example_function(A(), C()), 'works')
        self.assertEqual(example_function(E(), E()), 'works')


if __name__ == '__main__':
    unittest.main()
