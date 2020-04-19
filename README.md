## Description

`Polynomial` is a class used to create a polynomial from a list of tuples, which represents
the terms of the polynomial. Each tuple consists of two elements: the coefficient,
the first element, and the exponent, the second element.

The operations that can be performed are addition, subtraction, multiplication,
differentiation and integration.

## Usage

Import the class Polynomial from `src/polynomial.py`:

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

As an example, the following polynomial gives distinct primes for integers n such that 0 <= n <= 39:

```Python
x = Polynomial([(1,1)])
p = x**2 + x + 41

is_prime = lambda k: type(k) == int and k > 1 and not any(k%n == 0 for n in range(2,k))

# test should be equal to true
test = all(is_prime(p(k)) for k in range(40))
```

## Tests

Unit tests can be run with the following command:

```bash
python3 -m unittest discover -v
```