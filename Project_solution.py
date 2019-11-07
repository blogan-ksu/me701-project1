#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:35:19 2019

@author: student
"""
import scipy as sp
from scipy.optimize import minimize

#%%
# Given Values:
Sut = 590.0 # MPa
Sy = 490.0 # MPa

F_max = 15000.0 # Newtons
F_min = 5000.0 # Newtons

n = 1.2 # Safety Factor

#%%
# Loading Factors:
C_load = 0.7

A_95 = 0.05* 30 * 10 # mm^2
d_rect_area = sp.sqrt(A_95/0.076) # mm
C_size = 1.189*d_rect_area**(-0.097)

C_surface = 1.58 * (590**(-0.085))

C_temp = 1.0

C_reliab = 0.814

Se_prime = 0.5*Sut # MPa

def get_Se(Se_prime, C_load, C_size, C_surface, C_reliab, C_temp):
    ''' Returns the value of Se '''
    return Se_prime*C_load*C_size*C_surface*C_temp*C_reliab

Se = get_Se(Se_prime, C_load, C_size, C_surface, C_reliab, C_temp) # MPa

#%%
# Cycled Loads:
F_m = (F_max + F_min) / 2 # Newtons
F_a = (F_max - F_min) / 2 # Newtons

def get_sigma_m(d, F_m):
    '''Returns sigma m'''
    return F_m/(300 - 10 * d)

def get_sigma_a(d, F_a):
    '''Returns sigma a'''
    return F_a/(300 - 10 * d)

#%%
# Set up Minimize Equations/Constraints:
def diameter(d, Se, Sut, F_a, F_m, n):
    x = d/30
    sol = 30 - ( (Se + Sut) / (10*n*(F_a + F_m)) ) * \
          ( 1 / (3 - 3.14*(x) + 3.667*(x)**2 - 1.527*(x)**3))
    return sol


objective = lambda x: - diameter(x, Se, Sut, F_a, F_m, n)
constraint1 = lambda x: 30 - x
constraint2 = lambda x: (Sy / n) - (get_sigma_m(x, F_m) + get_sigma_a(x, F_a))

constraints = [{'type': 'ineq', 'fun': constraint1},
               {'type': 'ineq', 'fun': constraint2}]

d = 10.0 # mm (Initial Value)

#%%
# Run scipy.optimize.minimize

answer = minimize(objective, x0=d, constraints=constraints)
print(answer.x)


