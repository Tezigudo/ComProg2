"""This is test for function compose. that is every function in funclib.py"""

from unittest import TestCase
from funclib import *


class TestFunclip(TestCase):
    """TEst for every function in funclib module"""

    def setUp(self) -> None:
        self.f = lambda x: x**2
        self.g = lambda x: 1/x

    def test_identity(self):
        """Test for identity function"""
        self.assertEqual(identity(1, 2, 3), (1, 2, 3))
        self.assertEqual(identity("hello"), "hello")
        self.assertEqual(identity(), None)

    def test_apply(self):
        """Test for apply function"""
        self.assertEqual(apply(lambda x: x ** 2, [1, 2, 3]), [1, 4, 9])

    def test_inverse(self):
        """Test for inverse function"""
        for i in range(1, 100):
            self.assertAlmostEqual(inverse(identity)(i), 1/i, places=4)

    def test_compose(self):
        """Test for compose function"""

        for i in range(1, 100):
            self.assertAlmostEqual(compose(self.f, self.g)(i),
                                   self.f(self.g(i)), places=4)

    def test_oridinart_product(self):
        """Test for product function"""

        for i in range(1, 100):
            self.assertAlmostEqual(product(self.f, self.g)(i),
                                   self.f(i) * self.g(i), places=4)

    def test_product_more_parameters(self):
        """product with multiple parameter should work"""

        self.assertEqual(product(max, min)(1, 2, 3), 3)  # 3 * 1

    def test_polynomial(self):
        """Test for polynomial function"""

        constant = polynomial(4)
        # test constant
        self.assertEqual(constant(0), 4)

        line = polynomial(4, 1)  # 4x + 1

        # test linear equation
        for i in range(1, 100):
            self.assertEqual(line(i), 4*i + 1)

        parabola = polynomial(2, 0, 1)  # 2x**2 + 1

        # test parabola equation
        for i in range(1, 100):
            self.assertEqual(parabola(i), 2*i**2 + 1)

        # x**4 + (-2)*x**3 + (3)*x**2 + (-4)*x + 5
        cubic = polynomial(1, -2, 3, -4, 5)

        # test cubic equation
        for i in range(1, 100):
            self.assertEqual(cubic(i), (i**4 + (-2)*i**3 + (3)*i**2 + (-4)*i + 5))
