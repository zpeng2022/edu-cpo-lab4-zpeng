
# Different methods are used depending on the type of input parameter
from multi_method import multiple


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
