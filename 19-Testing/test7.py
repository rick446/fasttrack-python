import unittest

class MyTest(unittest.TestCase):

    def test_docstring(self):
        "This is a test docstring. It should say what's being tested."
        pass

    def test_no_docstring(self):
        pass

    def test_docstring_fail(self):
        "This is a test docstring. It should say what's being tested."
        assert False

    def test_no_docstring_fail(self):
        assert False

if __name__ == '__main__':
    unittest.main()
