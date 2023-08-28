import unittest
from fibonacci.fibonacci_tools import get_series

class TestStringMethods(unittest.TestCase):

    def test_nine_items(self):
        self.assertListEqual(get_series(9), [0,1,1,2,3,5,8,13,21])

    def test_three_items(self):
        self.assertListEqual(get_series(3), [0,1,1])
        
    def test_negative_items(self):
        self.assertRaises(ValueError, get_series, -1)

if __name__ == '__main__':
    unittest.main()
