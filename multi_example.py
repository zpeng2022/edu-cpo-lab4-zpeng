
# Different methods are used depending on the type of input parameter
from multi_method import multimethod


@multimethod(int, int)
def foo(a, b):
    return a + b


@multimethod(float, float)
def foo(a, b):
    return a - b


@multimethod(str, str)
def foo(a, b):
    return a + b


@multimethod(str)
@multimethod(str, int)
def foo(a, b=10):
    c = str(b)
    return a + c


@multimethod(float)
@multimethod(float, int)
@multimethod(float, int, int)
def foo(a, b=10, c=10):
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


@multimethod(A, D)
def foo(arg1, arg2):
   return 'works'


@multimethod(A, A)
def foo(arg1, arg2):
   return 'works'
