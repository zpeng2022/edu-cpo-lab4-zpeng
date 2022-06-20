import unittest
import math
from hypothesis import given
import hypothesis.strategies as st
import numpy as np

from multi_example import *


class TestMultimethod(unittest.TestCase):

    def test_matrix_add(self):
        a = np.ones((3, 4))
        b = np.zeros((3, 4))
        self.assertEqual(example_function(a, b),
                         np.add(a, b).tolist())

    def test_matrix_mul(self):
        a = np.ones((3, 4))
        b = np.zeros((4, 3))
        self.assertEqual(example_function_mul(a, b),
                         np.multiply(a, b).tolist())

    def test_matrix_mul(self):
        a = np.ones((3, 4))
        b = np.zeros((3, 4))
        self.assertEqual(example_function_div(b, a),
                         np.divide(b, a).tolist())

    @given(st.lists(st.integers(), min_size=1),
           st.lists(st.integers(), min_size=1))
    def test_matrix_add_integers(self, a, b):
        if len(a) > len(b):
            a = a[:len(b)]
        if len(b) > len(a):
            b = b[:len(a)]
        matrix_a = np.array(a)
        matrix_b = np.array(b)

        self.assertEqual(example_function(matrix_a, matrix_b),
                         np.add(matrix_a, matrix_b).tolist())

    @given(st.lists(st.integers(), min_size=1),
           st.lists(st.integers(), min_size=1))
    def test_matrix_mul_integers(self, a, b):
        if len(a) > len(b):
            a = a[:len(b)]
        if len(b) > len(a):
            b = b[:len(a)]
        matrix_a = np.array(a)
        matrix_b = np.array(b)
        self.assertEqual(example_function_mul(matrix_a, matrix_b),
                         np.multiply(matrix_a, matrix_b).tolist())

    @given(st.lists(st.integers()), st.lists(st.integers()))
    def test_matrix_div_integers(self, a, b):
        if len(a) > len(b):
            a = a[:len(b)]
        if len(b) > len(a):
            b = b[:len(a)]
        matrix_a = np.array(a)
        matrix_b = np.ones(len(a))
        self.assertEqual(example_function_div(matrix_a, matrix_b),
                         np.divide(matrix_a, matrix_b).tolist())

    def test_function_mul(self):
        self.assertEqual(example_function_mul(1), 1)
        self.assertEqual(example_function_mul(1, 3), 3)
        self.assertEqual(example_function_mul(1.0), 2.0)

    @given(st.integers(), st.integers())
    def test_function_mul_integers(self, a, b):
        self.assertEqual(example_function_mul(a), a)
        self.assertEqual(example_function_mul(a, b), a * b)

    @given(st.floats(), st.integers(), st.integers())
    def test_function_mul_float_integers(self, a, b, c):
        if math.isnan(a) is False and math.isinf(a) is False:
            self.assertEqual(example_function_mul(a), a * 2)
            self.assertEqual(example_function_mul(a, b), a * b * 2)
            self.assertEqual(example_function_mul(a, b, c), a * b * c)

    def test_function_div(self):
        self.assertEqual(example_function_div(4, 2), 2)
        self.assertEqual(example_function_div(4), 4)
        self.assertEqual(example_function_div(2.0), 1.0)

    @given(st.integers(), st.integers())
    def test_function_div_integers(self, a, b):
        self.assertEqual(example_function_div(a), float(a))
        if b != 0:
            self.assertEqual(example_function_div(a, b), float(a / b))

    @given(st.floats(), st.integers(), st.integers())
    def test_function_div_float_integers(self, a, b, c):
        if math.isnan(a) is False and math.isinf(a) is False\
                and b != 0 and c != 0:
            self.assertEqual(example_function_div(a), a / 2)
            self.assertEqual(example_function_div(a, b), a / (2 * b))
            self.assertEqual(example_function_div(a, b, c), a / (b * c))

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
