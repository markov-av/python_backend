import unittest
import gcd


class GcdTest(unittest.TestCase):
    """
    gcd take m: int, n: int

    """
    def test_gcd_return_n(self):
        self.assertEqual(gcd.gcd(0, 2), 2)

    def test_gcd_return_m(self):
        self.assertEqual(gcd.gcd(1, 0), 1)

    def test_gcd_same(self):
        self.assertAlmostEqual(gcd.gcd(1, 1), 1)

    def test_gcd_by_one(self):
        self.assertAlmostEqual(gcd.gcd(1, 4), 1)
        self.assertAlmostEqual(gcd.gcd(5, 1), 1)

    def test_gcd_1(self):
        self.assertAlmostEqual(gcd.gcd(10, 20), 10)

    def test_gcd_2(self):
        self.assertAlmostEqual(gcd.gcd(10, 11), 1)

    def test_gcd_3(self):
        self.assertAlmostEqual(gcd.gcd(10, 11), 1)
        self.assertAlmostEqual(gcd.gcd(11, 10), 1)


if __name__ == '__main__':
    unittest.main()
