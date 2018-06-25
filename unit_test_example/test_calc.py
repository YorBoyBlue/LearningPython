import unittest
from unit_test_example import calc


# You can execute the line below through the terminal to run the tests or just
# run the file with the __main__ check in it.
# python -m unittest unit_test_example.test_calc

class TestCalc(unittest.TestCase):

    # Unit test functions require a prefix of test_ to run
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # Check to make sure our exception is raised properly
        # self.assertRaises(ValueError, calc.divide, 10, 0)

        # Check to make sure our exception is raised properly using a context
        # manager to call function with it's proper signature
        with self.assertRaises(ValueError):
            calc.divide(10, 0)
            # this will produce the error
            # calc.divide(10, 2)


if __name__ == '__main__':
    unittest.main()
