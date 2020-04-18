## Description

`polynomial.py` contains the definition of a class that can be used to create
polynomials. Some of the operations that can be performed are addition, subtraction,
multiplication, differentiation and integration.
The terms of the polynomial are represented by a list of tuples. Each tuple consists of
two elements: the coefficient, the first element, and the exponent, the second element.

## Usage

Import the class Polynomial from polynomial.py:

```Python
from src.polynomial import Polynomial
```

Create a polynomial, for example x<sup>2</sup> + 3x + 1:

```Python
p = Polynomial([(1,0), (3,1), (1,2)])
```

or equivalently:

```Python
x = Polynomial([1,1])
p = x**2 + 3*x + 1
```

## Euler's prime-generating polynomial example

The follwing polynomial gives distinct primes for integers n such that 0 <= n <= 39:

```Python
x = Polynomial([(1,1)])
p = x**2 + x + 41

is_prime = lambda k: type(k) == int and k > 1 and not any(k%n == 0 for n in range(2,k))

# test should be equal to true
test = all(is_prime(p(k)) for k in range(40))
```

## Tests

Unit tests can be run from `polynomial` folder with the following command:

```bash
python3 -m unittest discover -v
```