# Python 3

class Polynomial:
    def __init__(self, terms):
        if type(terms) != list or any(type(t) != tuple or len(t) != 2 for t in terms):
            raise Exception('the terms must be a list of two-element tuples')
        if any(type(c) not in (int, float) for c, exp in terms):
            raise TypeError('every coefficient must be an integer or a float')
        if any(type(exp) != int for c, exp in terms):
            raise TypeError('every exponent must be an integer')
        self.terms = [t for t in sorted(terms, key = lambda x: x[1]) if t[0] != 0]
        self.degree = -1 if len(self.terms) == 0 else self.terms[-1][1]
    
    def evaluate(self, k):
        '''Substitute k to the indeterminate x and return the value of the
        resulting expression.
        '''
        if type(k) not in (int, float):
            raise TypeError('can only substitute an integer or a float to the indeterminate x')
        return sum((c*k**exp for c, exp in self.terms))
    
    def __repr__(self):
        return 'Polynomial({terms})'.format(terms = self.terms)
    
    def __str__(self):
        if self.degree == -1:
            return '0'
        else:
            s = ''
            for c, exp in reversed(self.terms):
                if c != 0:
                    s += ' - ' if c < 0 else ' + '
                    s += str(abs(c)) if (exp == 0 or abs(c) != 1) else ''
                    s += 'x' if exp > 0 else ''
                    s += '**' + str(exp) if exp > 1 else ''
            # the leading sign is included only if it is a minus
            return s[1:] if s[1] == '-' else s[3:]
    
    def __bool__(self):
        # return False if the Polynomial object is the zero polynomial, else True.
        return self.degree != -1
    
    def __eq__(self, other):
        if type(other) == Polynomial:
            return self.terms == other.terms
        elif type(other) in (int, float):
            return self.terms == [(other, 0)] * int(other != 0)
        else:
            return False
    
    def __add__(self, other):
        if type(other) not in (int, float, Polynomial):
            raise TypeError('%s object cannot be interpreted as a Polynomial' % type(other).__name__)
        other_polynomial = other if type(other) == Polynomial else Polynomial([(other, 0)])
        result = []
        i, j = 0, 0
        while i < len(self.terms) and j < len(other_polynomial.terms):
            if self.terms[i][1] < other_polynomial.terms[j][1]:
                result.append(self.terms[i])
                i += 1
            elif self.terms[i][1] > other_polynomial.terms[j][1]:
                result.append(other_polynomial.terms[j])
                j += 1
            else:
                result.append((self.terms[i][0] + other_polynomial.terms[j][0], self.terms[i][1]))
                i += 1
                j += 1
        if i == len(self.terms):
            return Polynomial(result + other_polynomial.terms[j:])
        else:
            return Polynomial(result + self.terms[i:])
    
    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if type(other) not in (int, float, Polynomial):
            raise TypeError('%s object cannot be interpreted as a Polynomial' % type(other).__name__)
        other_polynomial = other if type(other) == Polynomial else Polynomial([(other, 0)])
        return -1*other + self
    
    def __rsub__(self, other):
        return -1*self + other
    
    def __mul__(self, other):
        if type(other) not in (int, float, Polynomial):
            raise TypeError('%s object cannot be interpreted as a Polynomial' % type(other).__name__)
        other_polynomial = other if type(other) == Polynomial else Polynomial([(other, 0)])
        return sum((Polynomial([(c1 * c2, exp1 + exp2) for c1, exp1 in self.terms])
                   for c2, exp2 in other_polynomial.terms), Polynomial([]))
    
    def __rmul__(self, other):
        return self * other
    
    def __truediv__(self, other):
        from collections import namedtuple
        if type(other) not in (int, float, Polynomial):
            raise TypeError('%s object cannot be interpreted as a Polynomial' % type(other).__name__)
        other_polynomial = other if type(other) == Polynomial else Polynomial([(other, 0)])
        if self.degree < other_polynomial.degree:
            raise Exception('cannot divide a Polynomial by another of higher degree')
        if other_polynomial.degree == -1:
            raise ZeroDivisionError('cannot divide a Polynomial by the zero polynomial')
        # The quotient and the remainder are initialized as the zero polynomial
        # and the dividend itself, respectively
        quotient = Polynomial([])
        remainder = Polynomial(self.terms)
        while remainder.degree >= other_polynomial.degree:
            c = remainder.terms[-1][0] / other_polynomial.terms[-1][0]
            exp = remainder.terms[-1][1] - other_polynomial.terms[-1][1]
            temp = Polynomial([(c, exp)])
            quotient += temp
            remainder -= temp * other_polynomial
        # The result of the division is a namedtuple in order to better identify
        # the quotient and the remainder
        Polynomial_division = namedtuple('Polynomial_division', ['quotient', 'remainder'])
        return Polynomial_division(quotient = quotient, remainder = remainder)
    
    def __pow__(self, n):
        import functools
        if type(n) != int:
            raise TypeError('the exponent must be an integer')
        if n < 0:
            raise ValueError('the exponent must be greater than or equal to zero')
        return functools.reduce(lambda x,y: x*y , (Polynomial(self.terms) for i in range(n)), 1)
    
    def derivative(self, n=1):
        '''Return the nth derivative of the polynomial.'''
        import functools
        if type(n) != int:
            raise TypeError('the order of the derivative must be an integer')
        if n < 0:
            raise ValueError('the order of the derivative must be greater than or equal to zero')
        result = []
        for c, exp in self.terms:
            result.append((functools.reduce(lambda x,y: x*y, range(exp-n+1,exp+1), c), max(exp-n, 0)))
        return Polynomial(result)
    
    def integral(self, c=0):
        '''Return the primitive integral of the polynomial. The constant factor is equal to c.'''
        if type(c) not in (int, float):
            raise TypeError('the constant factor must be an integer or a float')
        result = [(c,0)] + [(c / (exp+1), exp+1) for c, exp in self.terms]
        return Polynomial(result)