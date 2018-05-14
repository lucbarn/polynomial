## Description

`polynomial.py` contains the definition of a class that can be used to create
polynomials. Some of the operations that can be performed are addition, subtraction,
multiplication, differentiation and integration.
The terms of the polynomial are represented by a list of tuples. Each tuple consists of
two elements: the coefficient, the first element, and the exponent, the second element.<br>
So, for example, the polynomial p, x<sup>2</sup> + 3x + 1, is initialized as

```Python
p = Polynomial([(1,0), (3,1), (1,2)])
```

or equivalently:

```Python
x = Polynomial([1,1])
p = x**2 + 3*x + 1
```

`test_cases.py` contains some test cases.

`utils.py` contains two functions that are used in `test_cases.py`.
