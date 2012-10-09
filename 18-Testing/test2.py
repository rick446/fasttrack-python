import unittest

class MyTest(unittest.TestCase):

    def test_fail(self):
        assert False

    def test_fail_message(self):
        assert False, 'This is an assertion message'

if __name__ == '__main__':
    unittest.main()
