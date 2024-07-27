#!/usr/bin/env python
import unittest
from parameterized import parameterized
from utils import access_nested_map
class TestStringMethods(unittest.TestCase):
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    @parameterized.expand([
        ({'a':{'b':1}}, ['a', 'b'], 1),
        ({'a':{'b':{'c':2}}}, ['a', 'b', 'c'], 2),
    ])
    def test_nested_map(self, nested_map, path, expected_res):
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected_res)
    
    @parameterized.expand([
        (10, 5, 2),
        (14, 2, 7),
        (3, 0, None)
    ])
    def test_div(self, x, y, expected):
        if expected is None:
            with self.assertRaises(ZeroDivisionError):
                x / y
        else:
            self.assertEqual(x / y, expected)

if __name__ == '__main__':
    unittest.main()
