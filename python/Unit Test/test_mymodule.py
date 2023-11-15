"""
Test My Module
"""
import unittest

from mymodule import square, double, add 

class TestSquare(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(square(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.
        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.
        

class TestDouble(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.

class TestAdd(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(add(0,0), 0) # test when 0+0 is given as input the output is 0.
        self.assertEqual(add(-99,1), -98) # test when -99+1 is given as input the output is -98.
        self.assertEqual(add(100,-99), 1) # test when 100-99 is given as input the output is 1.

unittest.main()