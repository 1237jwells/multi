import unittest
from factorial import factorial
from random import seed, sample
import math

class TestFactorial(unittest.TestCase):
    def test_basic_function(self):
        self.assertEqual(factorial(6), 720)

    def test_bad_input(self):
        self.assertRaises(ValueError, factorial, "cat")
        self.assertRaises(ValueError, factorial, -2)

    def test_random_integers(self):
        seed(0)
        data = sample(range(20), 10)
        for x in data:
            self.assertEqual(factorial(x), math.factorial(x))

    

class TestCodingStandards(unittest.TestCase):
    def test_code_quality(self):
        from pylint import epylint as lint
        (pylint_stdout, _) = lint.py_run("factoial.py", return_std=True)
        output = pylint_stdout.getvalue()
        offset = output.rfind(" been rated at ")
        if offset != -1:
            output = output[offset:]
            end = output.find('/')
            output = output[15:end]
            score = float(output)
            self.assertGreaterEqual(score, 8.5)
