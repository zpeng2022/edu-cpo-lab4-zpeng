[![Test Check](https://github.com/zpeng2022/edu-cpo-lab4-zpeng/actions/workflows/check.yml/badge.svg)](https://github.com/zpeng2022/edu-cpo-lab4-zpeng/actions/workflows/check.yml)

# slay_the_dragon - lab #4 - variant 2

This is an example project which demonstrates multi-dispatch

## Project structure

- `multi_example.py` -- implementation of multi-function by using `@multiple`
- `multi_method.py` -- implementation of `Multiple` class with
- basic hash map features
- `test_multiple_dispatch.py` -- tests for multiple_dispatch

## Features

- add test_type_integral
- add test_type_text
- add test_type_float
- add test_optial_int_text
- add test_optional_ints
- add test_optional_float_int
- add test_named_object_integers
- add test_named_object_text
- add test_named_object_float_int
- add test_function_mul
- add test_function_mul_integers
- add test_function_mul_float_integers
- add test_function_div
- add test_function_div_integers
- add test_function_div_float_integers

## Contribution

- Zhan,Peng (zpeng@hdu.edu.cn) -- write the main class part.
- Zhong,ZhuZhou(212320020@hdu.edu.cn) -- write the test part and README.md.

## Changelog

- 20.06.2022 - 5
  - add * and / and - operations for numeral
  - add more PBT tests for that
- 18.06.2022 - 4
  - add more tests
- 18.06.2022 - 3
  - disable the mypy check
  - because we need multi functions
- 18.06.2022 - 2
  - Update README.md
- 18.06.2022 - 1
  - add multi_example.py
  - add multi_method.py
  - add test_multiple_dispatch.py
- 18.06.2022 - 0
  - Initial

## Design notes

- Advantages of unit testing:
  - it help us write better code
  - it help us catch bugs earlier
  - it makes us more efficient at writing code
  - it make us detect regression bugs
- Disadvantage of unit testing:
  - it takes time to write cases
  - tests require a lot of time for maintenance
  - it can be challenging to test GUI code
  - unit testing can't catch all errors
- Advantages of PBT testing:
  - the PBT provides a reasonable estimate of the
  - evidential test result within the relevant forensic range
- Disadvantages of PBT testing:
  - it also be challenging to test GUI code
