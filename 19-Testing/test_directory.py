import unittest
import directory

class TestEmptyDirectory(unittest.TestCase):

    def setUp(self):
        self.d = directory.Directory()

    def test_add_number(self):
        self.d.add_number('name', '111.111.1111')
        self.assertEqual(
            self.d.lookup_number('name'),
            '111.111.1111')

    def test_lookup_unknown_number(self):
        self.assertRaises(KeyError, self.d.lookup_number, 'name')

    def test_remove_unknown_number(self):
        self.assertRaises(KeyError, self.d.remove_number, 'name')

    def test_repr_has_two_lines(self):
        d_repr = repr(self.d)
        self.assertEqual(len(d_repr.splitlines()), 2)

class TestNonemptyDirectory(unittest.TestCase):
    
    def setUp(self):
        self.d = directory.Directory()
        self.d.add_number('name', '111.111.1111')

    def test_lookup_number(self):
        self.assertEqual(
            self.d.lookup_number('name'),
            '111.111.1111')

    def test_remove_number(self):
        self.d.remove_number('name')
        self.assertRaises(KeyError, self.d.lookup_number, 'name')

    def test_repr_has_three_lines(self):
        d_repr = repr(self.d)
        self.assertEqual(len(d_repr.splitlines()), 3)

if __name__ == '__main__':
    unittest.main()
