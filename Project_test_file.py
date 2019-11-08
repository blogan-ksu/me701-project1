#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from Project_solution import get_Se
from Project_solution import get_sigma_m
from Project_solution import get_sigma_a
from Project_solution import answer

class Test_variables(unittest.TestCase):
    
    def test_get_Se(self):
        self.assertEqual(get_Se(295, 0.7, 0.9201547826571058, 0.9186173970642588, 0.814, 1), 142.08231173264952)
    
    def test_get_sigma_m(self):
        self.assertEqual(get_sigma_m(10, 10000, 30, 10), 50)
    
    def test_get_sigma_a(self):
        self.assertEqual(get_sigma_a(10, 5000, 30, 10), 25)
    
    def test_answer(self):
        self.assertEqual(float(answer.x), 16.70488651870801)


if __name__ == "__main__":
    unittest.main()
