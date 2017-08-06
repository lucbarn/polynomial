from polynomial import Polynomial
from utils import pascals_triangle, binomial_expansion

def test():

    x = Polynomial([(1,1)])

    assert x**0 == 1
    assert x**1 == 0 + x == x + 0 == x
    assert x - x == x * 0 == 0
    assert x + x == 2 * x
    assert (x+1)**2 == x**2 + 2 * x + 1
    assert (x**2 - 1) == (x - 1) * (x + 1)
    assert (x-4)**100 == binomial_expansion(x,-4,100)
    assert x.derivative().integral() == x.integral().derivative() == x

    # test cases for polynomial long division

    den1 = x**2 + 2*x + 3
    q1 = 2*x
    r1 = x + 5
    num1 = den1 * q1 + r1
    div1 = num1 / den1
    assert num1 == den1 * div1.quotient + div1.remainder

    den1 = 9 * x**4 + 6 * x**3 + 2 * x**2 + 4 * x
    q1 = 2 * x**2 + 2 * x + 5
    r1 = x**2 + 4
    num1 = den1 * q1 + r1
    div1 = num1 / den1
    assert num1 == den1 * div1.quotient + div1.remainder


if __name__ == '__main__':
    test()
    print('Test passed!')
