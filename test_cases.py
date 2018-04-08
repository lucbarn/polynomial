import unittest
from polynomial import Polynomial
from utils import pascals_triangle, binomial_expansion
from random import randint


class TestPolynomialMethods(unittest.TestCase):

    def setUp(self):
        self.x = Polynomial([(1,1)])

    def test_zero_power(self):
        self.assertEqual(self.x**0, 1, 'x**0 should be equal to 1')

    def test_one_power(self):
        self.assertEqual(self.x**1, self.x, 'x**1 should be equal to x')

    def test_zero_sum(self):
        self.assertEqual(self.x + 0, self.x, 'x+0 should be equal to x')

    def test_self_difference(self):
        self.assertEqual(self.x - self.x, 0, 'x-x should be equal to 0')

    def test_sum_product_equivalence(self):
        self.assertEqual(self.x + self.x, self.x * 2, 'x+x should be equal to 2x')

    def test_derivative_integral_concatenation(self):
        self.assertEqual(self.x.derivative().integral(),
                         self.x,
                         'the integral of the derivative of x should be equal to x')


class TestPolynomialExpansion(unittest.TestCase):

    def setUp(self):
        self.x = Polynomial([(1,1)])

    def test_square_binomial(self):
        self.assertEqual((self.x + 1) ** 2, self.x**2 + 2 * self.x + 1, '(x+1)**2 should be equal to x**2 + 2x + 1')

    def test_cube_binomial(self):
        self.assertEqual((self.x - 1) ** 3,
                    self.x**3 - 3 * self.x**2 + 3 * self.x - 1,
                    '(x-1)**3 should be equal to x**3 - 3x**2 + 3x - 1')

    def test_difference_squares(self):
        self.assertEqual((self.x**2 - 1),
                    (self.x + 1) * (self.x - 1),
                    'x**2 - 1 should be equal to (x+1) * (x-1)')

    def test_big_exponent(self):
        self.assertEqual((self.x - 4) ** 100,
                    binomial_expansion(self.x, -4, 100),
                    '(x-4)**100 should be equal to the binomial expansion of (x-4) computed using Pascal\'s triangle')


class TestPolynomialLongDivision(unittest.TestCase):

    def setUp(self):
        self.x = Polynomial([(1,1)])

    def test_division_1(self):
        den = self.x**2 + 2 * self.x + 3
        q = 2 * self.x
        r = self.x + 5
        num = den * q + r
        div = num / den
        self.assertEqual(num, den * div.quotient + div.remainder)

    def test_division_2(self):
        den = 9 * self.x**4 + 6 * self.x**3 + 2 * self.x**2 + 4 * self.x
        q = 2 * self.x**2 + 2 * self.x + 5
        r = self.x**2 + 4
        num = den * q + r
        div = num / den
        self.assertEqual(num, den * div.quotient + div.remainder)


class TestPolynomialDegree(unittest.TestCase):

    def setUp(self):
        self.p = Polynomial([])
        self.x = Polynomial([(1,1)])

    def test_polynomial_degree(self):
        for n in range(100):
            self.p += randint(1,10) * self.x**n
            self.assertEqual(self.p.degree(), n)


if __name__ == '__main__':
    unittest.main()
