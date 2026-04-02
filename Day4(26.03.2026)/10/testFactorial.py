import pract_2
import unittest

print(pract_2.factorial(-1))

class TestFact(unittest.TestCase):
    def testFactorial(self):
        result_5 = pract_2.factorial(5)
        result_0 = pract_2.factorial(0)
        result_1 = pract_2.factorial(1)
        result_type = pract_2.factorial("abc")
        result_neg = pract_2.factorial(-2)

        self.assertEqual(result_5, 120)
        self.assertEqual(result_0, 1)
        self.assertEqual(result_1, 1)
        self.assertEqual(result_type, -1)
        self.assertEqual(result_neg, -1)