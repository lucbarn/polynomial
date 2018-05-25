import unittest
from utils import pascals_triangle, binomial_expansion

class TestPascalsTriangle(unittest.TestCase):

    def test_first_row(self):
        self.assertEqual(
            pascals_triangle(0),
            [1],
            'first row should contain only 1'
        )

    def test_second_row(self):
        self.assertEqual(
            pascals_triangle(1),
            [1,1],
            'second row should contain two elements equal to 1'
        )

    def test_eigth_row(self):
        self.assertEqual(
            pascals_triangle(7),
            [1,7,21,35,35,21,7,1],
            'eigth row should contain 1,7,21,35,35,21,7,1'
        )

    def test_symmetrical_row(self):
        for n in range(20):
            row = pascals_triangle(n)
            first_half = row[:(len(row) // 2)]
            second_half = row[((len(row) + 1) // 2):]
            self.assertEqual(
                first_half,
                list(reversed(second_half)),
                'every row of the triangle should be symmetrical'
            )

class TestBinomialExpansion(unittest.TestCase):

    def test_power_zero(self):
        self.assertEqual(
            binomial_expansion(1,2,0),
            1,
            'a binomial raised to the power of zero should be equal to 1'
        )

    def test_power_one(self):
        self.assertEqual(
            binomial_expansion(-2,4,1),
            -2+4,
            'a binomial raised to the power of 1 should be equal to itself'
        )

if __name__ == '__main__':
    unittest.main()
