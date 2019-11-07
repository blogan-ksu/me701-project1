#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:35:19 2019

@author: student
"""

import scipy as sp
from scipy.optimize import minimize

# Loading Factors:
d = 10
C_load = 0.7

A_95 = 0.05* 30 * 10 
d_rect_area = sp.sqrt(A_95/0.076)
C_size = 1.189*d_rect_area**(-0.097)

C_surface = 1.58 * (590**(-0.085))

C_temp = 1

C_reliab = 0.814

Se_prime = 0.5*590

def Se(Se_prime, C_load, C_size, C_surface, C_reliab, C_temp):
    ''' Returns the value of Se '''
    return Se_prime*C_load*C_size*C_surface*C_temp*C_reliab

Se = Se(Se_prime, C_load, C_size, C_surface, C_reliab, C_temp)

F_max = 15000 # Newtons
F_min = 5000 # Newtons
F_m = (F_max + F_min) / 2
F_a = (F_max - F_min) / 2

Sy = 490
n = 1.2

def sigma_m(d, F_m):
    '''Returns sigma m'''
    return F_m/(300 - 10 * d)

def sigma_a(d, F_a):
    '''Returns sigma a'''
    return F_a/(300 - 10 * d)

def actual_stress(Se, d, F_a, F_m):
    return (Se*((F_a/(300-10*d)) + (F_m/(300-10*d))) * 1/(3-3.14*(d/30)+3.667*(d/30)**2-1.527*(d/30)**3))

objective = lambda x: - actual_stress(Se, x[0], F_a, F_m)
constraint1 = lambda x: 30 - x[0]
constraint2 = lambda x: (Sy / n) - (sigma_m(x[0], F_m) + sigma_a(x[0], F_a))

constraints = [{'type': 'ineq', 'fun': constraint1},
               {'type': 'ineq', 'fun': constraint2},
               {'type': 'ineq', 'fun': constraint3}]
answer = minimize(objective, x0=[d], constraints=constraints)
print(answer.x)


