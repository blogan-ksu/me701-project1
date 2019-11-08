#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from Project_solution import get_Se, answer, diameter, get_sigma_m,\
                             get_sigma_a, get_sigma_max

class Test_variables(unittest.TestCase):
    
    def test_get_Se(self):
        '''
        This tests that a valid result is given by the get_Se function.
        '''
        
        self.assertAlmostEqual(get_Se(295, 0.7, 0.9201547826571058, 0.9186173970642588, 0.814, 1), 142.08231173264952)
    
    def test_get_sigma_m(self):
        '''Tests that get_sigma_m returns correct mean stress.'''
        self.assertAlmostEqual(get_sigma_m(10, 10000, 30, 10), 50)
    
    def test_get_sigma_a(self):
        '''Tests that get_sigma_a returns correct stress amplitude.'''
        self.assertAlmostEqual(get_sigma_a(10, 5000, 30, 10), 25)
        
    def test_get_sigma_max(self):
        '''Tests that get_sigma_max returns correct stress amplitude.'''
        self.assertAlmostEqual(get_sigma_max(10, 10000, 5000, 30, 10), 75)
    
    def test_valid_diameter(self):
        ''' 
        This ensures that the diameter solved for by scipy.optimize.minimize
        is equal to the diameter solved for by the diameter function.
        '''
        
        x = float(answer.x)
        Se = get_Se(295, 0.7, 0.9201547826571058, 0.9186173970642588, 0.814, 1)
        self.assertAlmostEqual(x,\
                               diameter(x, Se, 590, 5000, 10000, 1.2, 30, 10),\
                               places=4)
        
    def test_for_yielding(self):
        '''
        This tests to make sure that yielding will not occur at the diameter
        that has been sovled for.
        '''
        x = float(answer.x) / 30.0
        k_t = (3 - 3.14*(x) + 3.667*(x)**2 - 1.527*(x)**3)
        sigma_max = get_sigma_max(float(answer.x), 10000, 5000, 30, 10)
        A = 300-10*float(answer.x)
        self.assertLess(k_t*sigma_max/A, 490)

    def test_for_safety_factor(self):
        '''
        This tests to make sure that the maximum stress at the solved diameter
        is less than the allowable strength accounted for by the safety factor.
        '''
        x = float(answer.x) / 30.0
        k_t = (3 - 3.14*(x) + 3.667*(x)**2 - 1.527*(x)**3)
        sigma_max = get_sigma_max(float(answer.x), 10000, 5000, 30, 10)
        A = 300-10*float(answer.x)
        self.assertLess(k_t*sigma_max/A, 490/1.2)
        
        
if __name__ == "__main__":
    unittest.main()
