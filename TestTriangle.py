# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInvalidInputs(self): # all works
        self.assertEqual(classifyTriangle(-1, 2, 3), 'InvalidInput', 'Negative side should be invalid')
        self.assertEqual(classifyTriangle(201, 2, 3), 'InvalidInput', 'Side greater than 200 should be invalid')
        self.assertEqual(classifyTriangle(1.5, 2, 3), 'InvalidInput', 'Non-integer side should be invalid')
        self.assertEqual(classifyTriangle(0, 2, 3), 'InvalidInput', 'Zero side should be invalid')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle', 'Sum of two sides is less than the third side') 
        self.assertEqual(classifyTriangle(3, 3, 9), 'NotATriangle', 'Sum of two sides is equal to the third side')

    def testRightTriangles(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5,12,13 is a Right triangle')
        self.assertEqual(classifyTriangle(13, 5, 12), 'Right', 'Order of sides should not affect right triangle detection')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene', '3,4,5 is a scalene triangle')
        self.assertEqual(classifyTriangle(6, 8, 11), 'Scalene', '6,8,10 is a scalene triangle')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles', '2,2,3 is an isosceles triangle')
        self.assertEqual(classifyTriangle(7, 10, 10), 'Isosceles', '7,10,10 is an isosceles triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', '10,10,10 should be equilateral')







if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

