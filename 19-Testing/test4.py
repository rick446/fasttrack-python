import unittest
import simple_math

class MyTest(unittest.TestCase):

    def test_one_and_one_alt(self):
        try:
            simple_math.divide(1,0)
        except ZeroDivisionError:
            pass
        else:
            raise AssertionError, 'Exception was not raised'

    def test_one_and_one(self):
        self.assertRaises(ZeroDivisionError, simple_math.divide, 1, 0)


if __name__ == '__main__':
    unittest.main()
