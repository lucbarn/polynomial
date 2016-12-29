# Python 3.4.2

class Polynomial:
    '''Given an input tuple (or list, which is then converted to a tuple) create
    a polynomial in a single indeterminate x.
    The nth element of the input tuple is the coeffcient of the nth power of x.
    '''

    def __init__(self, coefs):
        # The unnecessary zeros to the right of the rightmost non-zero coefficient
        # are deleted, unless the Polynomial object is the zero polynomial.
        i = len(coefs) - 1
        while i > 0:
            if coefs[i] == 0:
                i -= 1
            else:
                break
        self.coefs = tuple(coefs[:(i+1)])

    def evaluate(self, k):
        '''Substitute k to the indeterminate x and return the value of the
        resulting expression.
        '''
        return sum([self.coefs[i] * k**i for i in range(len(self.coefs))])

    def __repr__(self):
        return 'Polynomial({coefficients})'.format(coefficients = self.coefs)

    def __str__(self):
        if self.coefs == (0,):
            return '0'
        else:
            s = ''
            for i in reversed(range(len(self.coefs))):
                if self.coefs[i] != 0:
                    s += ' - ' if (self.coefs[i] < 0) else ' + '
                    s += str(abs(self.coefs[i])) if (i == 0 or abs(self.coefs[i]) != 1) else ''
                    s += 'x' if (i > 0) else ''
                    s += '**' + str(i) if (i > 1) else ''
            return s[1:] if s[1] == '-' else s[3:]

    def __bool__(self):
        '''Return False if the Polynomial object is the zero polynomial, else True.'''
        return self.coefs[-1] != 0

    def __eq__(self, other):
        if type(other) == Polynomial:
            return self.coefs == other.coefs
        elif type(other) in [int, float]:
            return self == Polynomial((other,))
        else:
            return False

    def __add__(self, other):
        assert type(other) in [int, float, Polynomial]
        other_polynomial = Polynomial((other,)) if type(other) in [int, float] else other
        m = min(len(self.coefs), len(other_polynomial.coefs))
        t = tuple(self.coefs[i] + other_polynomial.coefs[i] for i in range(m))
        r = self.coefs[m:] + other_polynomial.coefs[m:]
        return Polynomial(t+r)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        assert type(other) in [int, float, Polynomial]
        other_polynomial = Polynomial((other,)) if type(other) in [int, float] else other
        return -1*other + self

    def __rsub__(self, other):
        return -1*self + other

    def __mul__(self, other):
        assert type(other) in [int, float, Polynomial]
        other_polynomial = Polynomial((other,)) if type(other) in [int, float] else other
        def inner_function(c,m,i):
            t = ()
            for j in range(len(c)):
                t += (c[j] * m,)
            return (0,)*i + t
        output = Polynomial(inner_function(self.coefs, other_polynomial.coefs[0], 0))
        for i in range(1,len(other_polynomial.coefs)):
            output += Polynomial(inner_function(self.coefs, other_polynomial.coefs[i], i))
        return output

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        import collections
        other_polynomial = Polynomial((other,)) if type(other) in [int, float] else other
        assert len(self.coefs) >= len(other_polynomial.coefs)
        # The quotient and the remainder are initialized as the zero polynomial
        # and the dividend itself, respectively
        quotient = Polynomial((0,))
        remainder = Polynomial(self.coefs)
        while len(remainder.coefs) >= len(other_polynomial.coefs):
            temp = Polynomial((0,) * (len(remainder.coefs) - len(other_polynomial.coefs))
                              + (remainder.coefs[-1] / other_polynomial.coefs[-1],))
            quotient += temp
            remainder -= (temp * other_polynomial)
        # The result of the division is a namedtuple in order to better identify
        # the quotient and the remainder
        Polynomial_division = collections.namedtuple('Polynomial_division',
                                                     ['quotient', 'remainder'])
        return Polynomial_division(quotient = quotient, remainder = remainder)

    def __pow__(self, n):
        assert n >= int(all(i == 0 for i in self.coefs)) and type(n) == int
        p = Polynomial(self.coefs)
        output = Polynomial((1,))
        for i in range(n):
            output *= p
        return output

    def derivative(self, n=1):
        '''Return the nth derivative of the polynomial.'''
        assert n >= 0 and type(n) == int
        p = Polynomial(self.coefs)
        for i in range(n):
            p = Polynomial(tuple(p.coefs[i] * i for i in range(1,len(p.coefs))))
        return p

    def integral(self, c=0):
        '''Return the primitive integral of the polynomial. The constant factor is equal to c.'''
        return Polynomial((c,) + tuple(self.coefs[i] / (i+1) for i in range(len(self.coefs))))
