# Python 3

# Test cases for polynomial.py

from polynomial import Polynomial

def test():

    x = Polynomial([(1,1)])

    assert x**0 == 1
    assert x**1 == 0 + x == x + 0 == x
    assert x - x == x * 0 == 0
    assert x + x == 2 * x
    assert (x+1)**2 == x**2 + 2 * x + 1
    assert (x**2 - 1) == (x - 1) * (x + 1)
    assert x.derivative().integral() == x.integral().derivative() == x

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

    def binomial_expansion(a,b,n):

        def pascals_triangle(m):
            levels = [[1], [1,1]]
            for i in range(2,m+1):
                temp = [levels[-1][j-1] + levels[-1][j] for j in range(1,len(levels[-1]))]
                levels.append([1] + temp + [1])
            return levels[m]

        coefficients = pascals_triangle(n)

        output = 0
        for k in range(n+1):
            output += coefficients[k] * (a**k) * (b**(n-k))
        return output

    assert (x-4)**100 == binomial_expansion(x,-4,100)


if __name__ == '__main__':
    test()
    print('Test passed!')
