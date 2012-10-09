import unittest

class MyTest(unittest.TestCase):

    def test_pass(self):
        pass

    def test_fail(self):
        assert False

    def test_also_fail(self):
        raise AssertionError

    def test_error(self):
        raise ValueError

if __name__ == '__main__':
    unittest.main()
