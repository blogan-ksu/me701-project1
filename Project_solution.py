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

w = 30.0 # mm
h = 10.0 # mm

n = 1.2 # Safety Factor

#%%
# Loading Factors:
C_load = 0.7

A_95 = 0.05* w * h # mm^2
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

def get_sigma_m(d, F_m, w, h):
    '''Returns sigma m'''
    return F_m/(w*h - h*d)

def get_sigma_a(d, F_a, w, h):
    '''Returns sigma a'''
    return F_a/(w*h - h*d)

#%%
# Set up Minimize Equations/Constraints:
def diameter(d, Se, Sut, F_a, F_m, n, w):
    x = d/w
    k_t = (3 - 3.14*(x) + 3.667*(x)**2 - 1.527*(x)**3)
    sol = 30 - k_t*n*0.1*( F_a/Se + F_m/Sut )
    return sol


objective = lambda x: - diameter(x, Se, Sut, F_a, F_m, n, w)

constraint1 = lambda x: w - x
constraint2 = lambda x: (Sy / n) - (F_max / (w*h - h*x)) * \
                        (3 - 3.14*(x/w) + 3.667*(x/w)**2 - 1.527*(x/w)**3)
constraint3 = lambda x: diameter(x, Se, Sut, F_a, F_m, n, w) - x
                        
constraints = [{'type': 'ineq', 'fun': constraint1},
               {'type': 'ineq', 'fun': constraint2},
               {'type': 'eq', 'fun': constraint3}]

d = 10.0 # mm (Initial Value)

#%%
# Run scipy.optimize.minimize

answer = minimize(objective, x0=d, constraints=constraints)
print(answer.x)


