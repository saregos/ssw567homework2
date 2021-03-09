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
    
    
    def testInvalidInputA(self): 
        self.assertEqual(classifyTriangle('a',1,1),'InvalidInput','\'a\',1,1 should be invalid')
    
    def testInvalidInputB(self): 
        self.assertEqual(classifyTriangle(1,-1,1),'InvalidInput','1,-1,1 should be invalid')
    
    def testInvalidInputC(self): 
        self.assertEqual(classifyTriangle(1,1,'a'),'InvalidInput','1,1,\'a\' should be invalid')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle')
        
    def testNotTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,2),'NotATriangle','1,1,2 should be Not a Triangle')
        
    def testNotTriangleB(self): 
        self.assertEqual(classifyTriangle(1,2,1),'NotATriangle','1,2,1 should be Not a Triangle')
        
    def testNotTriangleC(self): 
        self.assertEqual(classifyTriangle(2,1,1),'NotATriangle','2,1,1 should be Not a Triangle')
        
    def testScaleneTriangle(self): 
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 should be Scalene')
        
    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(2,2,3),'Isoceles','2,2,3 should be Isoceles')
        
    def testIsocelesTriangleB(self): 
        self.assertEqual(classifyTriangle(2,3,2),'Isoceles','2,3,2 should be Isoceles')
        
    def testIsocelesTriangleC(self): 
        self.assertEqual(classifyTriangle(3,2,2),'Isoceles','3,2,2 should be Isoceles')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

