# slay_the_dragon - lab #4 - variant 2

This is an example project which demonstrates multi-dispatch

## Project structure

- `multi_example.py` -- implementation of `DicHashMap` class with
- required features
- `multi_method.py` -- implementation of `SelfHashMap` class with
- basic hash map features
- `test_multiple_dispatch.py` -- tests for multiple_dispatch

## Features


## Contribution

- Zhan,Peng (zpeng@hdu.edu.cn) -- write the main class part.
- Zhong,ZhuZhou(212320020@hdu.edu.cn) -- write the test part and README.md.

## Changelog

- 18.06.2022 - 2
  - Update README.md
- 18.06.2022 - 1
  - add multi_example.py
  - add multi_method.py
  - add test_multiple_dispatch.py
- 18.06.2022 - 0
  - Initial

## Design notes

- DicHashMap and SelfHashMap
- HashMap is below the dic
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
