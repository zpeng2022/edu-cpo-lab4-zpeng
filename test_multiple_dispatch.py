import unittest
import math
from hypothesis import given
import hypothesis.strategies as st

from multi_example import *


class TestMultimethod(unittest.TestCase):

    # 1.Run different functions for different types
    def test_type_unittest(self):
        self.assertEqual(example_function('1', 10), '110')
        self.assertEqual(example_function(1, 2), 3)
        self.assertEqual(example_function(2.0, 1.0), 1.0)
        self.assertEqual(example_function('hello', ' world'), 'hello world')

    @given(st.integers(), st.integers())
    def test_type_integral(self, a, b):
        self.assertEqual(example_function(a, b), (a + b))

    @given(st.text(), st.text())
    def test_type_text(self, a, b):
        self.assertEqual(example_function(a, b), (a + b))

    @given(st.floats(), st.floats())
    def test_type_float(self, a, b):
        if (math.isnan(a) is False) and (math.isnan(b) is False)\
                and (math.isinf(a) is False) and (math.isinf(b) is False):
            self.assertEqual(example_function(a, b), (a - b))

    # 2.Optional and named parameters
    def test_optional_unittest(self):
        self.assertEqual(example_function('1'), '110')
        self.assertEqual(example_function(''), '10')
        self.assertEqual(example_function('1', 9), '19')

        self.assertEqual(example_function(1.0, 9, 10), 20)
        self.assertEqual(example_function(1.0), 21.0)
        self.assertEqual(example_function(1.0, 9), 20)

    @given(st.text(), st.integers())
    def test_optional_int_text(self, b, a):
        self.assertEqual(example_function(b), (b + str(10)))
        self.assertEqual(example_function(b, a), b + str(a))

    @given(st.integers(), st.integers())
    def test_optional_ints(self, a, b):
        self.assertEqual(example_function(1.0, a, b), 1.0 + a + b)
        self.assertEqual(example_function(1.0, a), 1.0 + a + 10)

    @given(st.integers(), st.integers(), st.floats())
    def test_optional_float_int(self, a, b, c):
        if math.isnan(c) is False and math.isinf(c) is False:
            self.assertEqual(example_function(c, a, b), c + a + b)
            self.assertEqual(example_function(c, a), c + a + 10)

    # 3.support for named argumants
    def test_named_object(self):
        self.assertEqual(example_function(a=3, b=2), 5)
        self.assertEqual(example_function(a='1', b=19), '119')

    @given(st.integers(), st.integers())
    def test_named_object_integers(self, c, d):
        self.assertEqual(example_function(a=0, b=0), 0)
        self.assertEqual(example_function(a=c, b=d), c + d)
        self.assertEqual(example_function(a='1', b=c), str(1) + str(c))

    @given(st.text(), st.text())
    def test_named_object_text(self, c, d):
        self.assertEqual(example_function(a=c, b=d), c + d)
        self.assertEqual(example_function('1', b=d), str(1) + str(d))

    @given(st.integers(), st.integers(), st.floats())
    def test_named_object_float_int(self, a, b, c):
        if math.isnan(c) is False and math.isinf(c) is False:
            self.assertEqual(example_function(a=c, b=a, c=b), c + a + b)
            self.assertEqual(example_function(a=c, b=a), c + a + 10)

    # 4.inherit
    def test_inherit(self):
        self.assertEqual(example_function(A(), A()), 'succeed!')
        self.assertEqual(example_function(A(), B()), 'succeed!')
        self.assertEqual(example_function(A(), C()), 'succeed!')
        self.assertEqual(example_function(E(), E()), 'succeed!')


if __name__ == '__main__':
    unittest.main()
