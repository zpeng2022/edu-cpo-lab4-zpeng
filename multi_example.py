
# Different methods are used depending on the type of input parameter
from multi_method import multiple
import numpy as np


@multiple(int, int)
def example_function(a, b):
    return a + b


@multiple(float, float)
def example_function(a, b):
    return a - b


@multiple(str, str)
def example_function(a, b):
    return a + b


@multiple(str)
@multiple(str, int)
def example_function(a, b=10):
    c = str(b)
    return a + c


@multiple(float)
@multiple(float, int)
@multiple(float, int, int)
def example_function(a, b=10, c=10):
    return a + b + c


@multiple(int, int)
def example_function_mul(a, b):
    return a * b


@multiple(int)
def example_function_mul(a, b=1):
    return a * b


@multiple(float)
@multiple(float, int)
@multiple(float, int, int)
def example_function_mul(a, b=1, c=2):
    return a * b * c


@multiple(int, int)
def example_function_div(a, b):
    return float(a / b)


@multiple(int)
def example_function_div(a, b=1):
    return float(a / b)


@multiple(float)
@multiple(float, int)
@multiple(float, int, int)
def example_function_div(a, b=1, c=2):
    return a / (b * c)


@multiple(np.ndarray, np.ndarray)
def example_function(a, b):
    return np.add(a, b).tolist()


@multiple(np.ndarray, np.ndarray)
def example_function_mul(a, b):
    return np.multiply(a, b).tolist()


@multiple(np.ndarray, np.ndarray)
def example_function_div(a, b):
    return np.divide(a, b).tolist()


class A(object):
  pass


class B(A):
  pass


class C(B):
  pass


class D(object):
  pass


class E(A, D):
  pass


@multiple(A, D)
def example_function(arg1, arg2):
   return 'succeed!'


@multiple(A, A)
def example_function(arg1, arg2):
   return 'succeed!'
