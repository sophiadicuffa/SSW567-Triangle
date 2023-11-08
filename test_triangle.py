"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from classify_triangle import classify_triangle


class TestTriangles(unittest.TestCase):
    '''define multiple sets of tests as functions with names that begin'''

    def test_invalid_inputs(self):
        '''tests invalid input cases'''
        self.assertEqual(classify_triangle(-1, 2, 3),
                         'InvalidInput', 'Negative side should be invalid')
        self.assertEqual(classify_triangle(201, 2, 3), 'InvalidInput',
                         'Side greater than 200 should be invalid')
        self.assertEqual(classify_triangle(1.5, 2, 3),
                         'InvalidInput', 'Non-integer side should be invalid')
        self.assertEqual(classify_triangle(0, 2, 3),
                         'InvalidInput', 'Zero side should be invalid')

    def test_not_a_triangle(self):
        '''tests not a triangle cases'''
        self.assertEqual(classify_triangle(1, 1, 3), 'NotATriangle',
                         'Sum of two sides is less than the third side')
        self.assertEqual(classify_triangle(3, 3, 9), 'NotATriangle',
                         'Sum of two sides is equal to the third side')

    def test_right_triangles(self):
        '''tests right triangle cases'''
        self.assertEqual(classify_triangle(3, 4, 5), 'Right',
                         '3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(5, 12, 13),
                         'Right', '5,12,13 is a Right triangle')
        self.assertEqual(classify_triangle(13, 5, 12), 'Right',
                         'Order of sides should not affect right triangle detection')

    def test_scalene_triangles(self):
        '''tests scalene triangle cases'''
        self.assertEqual(classify_triangle(3, 4, 6), 'Scalene',
                         '3,4,5 is a scalene triangle')
        self.assertEqual(classify_triangle(6, 8, 11),
                         'Scalene', '6,8,10 is a scalene triangle')

    def test_isosceles_triangles(self):
        '''tests isosceles triangle cases'''
        self.assertEqual(classify_triangle(2, 2, 3),
                         'Isosceles', '2,2,3 is an isosceles triangle')
        self.assertEqual(classify_triangle(7, 10, 10),
                         'Isosceles', '7,10,10 is an isoscele triangle')

    def test_equilateral_triangles(self):
        '''tests equialateral triangle cases'''
        self.assertEqual(classify_triangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')
        self.assertEqual(classify_triangle(10, 10, 10),
                         'Equilateral', '10,10,10 should be equilateral')
        
    def test_invalid_input_200(self):
        # Test case where one side is greater than or equal to 200
        self.assertEqual(classify_triangle(201, 100, 150), 'InvalidInput')
        self.assertEqual(classify_triangle(100, 201, 150), 'InvalidInput')
        self.assertEqual(classify_triangle(100, 150, 200), 'InvalidInput')

    def test_invalid_input_less_than_or_equal_to_0(self):
        # Test case where one side is less than or equal to 0
        self.assertEqual(classify_triangle(-1, 5, 10), 'InvalidInput')
        self.assertEqual(classify_triangle(5, -1, 10), 'InvalidInput')
        self.assertEqual(classify_triangle(5, 10, 0), 'InvalidInput')
        self.assertEqual(classify_triangle(-1, -1, -1), 'InvalidInput')

    def test_invalid_input_non_integer(self):
        # Test case where at least one side is not an integer
        self.assertEqual(classify_triangle('a', 5, 10), 'InvalidInput')
        self.assertEqual(classify_triangle(5, 10, 3.14), 'InvalidInput')
        self.assertEqual(classify_triangle(5.5, 10, 3), 'InvalidInput')

    def test_not_a_triangle_a(self):
        self.assertEqual(classify_triangle(100, 3, 1), 'NotATriangle')  # Sum of two sides is less than the third side
    def test_not_a_triangle_b(self):
        self.assertEqual(classify_triangle(1, 300, 1), 'NotATriangle')  # Sum of two sides is less than the third side
    


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
