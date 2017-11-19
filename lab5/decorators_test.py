import unittest
import time
from decorators import memorize
from decorators import profile
from decorators import convolve


class TestMidSkipQueue(unittest.TestCase):
    def test_decorators(self):
        @memorize
        @profile
        def function_with_decorators(param1, param2):
            time.sleep(2)

        function_with_decorators(1, 2)
        function_with_decorators(1, 2)

    def test_convolve_decorator(self):
        @convolve(3)
        def f(some_argument):
            return 2 * some_argument

        x = 3
        self.assertEqual(f(x), 2 * (2 * (2 * x)))

        self.assertRaises(AssertionError, convolve, 2.2)
        self.assertRaises(AssertionError, convolve, -1)


if __name__ == '__main__':
    unittest.main()
