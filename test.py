!/usr/bin/python3
# test case fro adding two numbers
import unittest

from prog1 import summation

class testsum(unittest.TestCase):
    def test_list_int(self):
        """
        test case to add two numbers
        """
        data=[23,32]
        result=summation(data)
        self.assertEqual(result,55)

if __name__=='__main__':
    unittest.main()
