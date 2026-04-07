# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:19:31 2026

@author: ezarazua
"""

import numpy as np

# Create a synthetic bioreactor function
l
def synthetic_bioreactor(temp, ph):
    """
    A sysnthetic objective function simulating mAb titer based on temperature 
    and pH.
    This is a multivarate quadratic (parabolic) response surface.
    
    Parameters
    ----------
    temp : float number
        Temperature range of the bioreactor.
    ph : float number
        pH value range of the bioreactor.

    Returns the expected maximum mAb titer 
    """
    # Optimal condiditions
    opt_temp = 37.0
    opt_ph = 7.2
    
    # Maximum possible titer in g/L
    max_titer = 5.0
    
    # Sensitivity coefficients (how fast titer drops off when moving away from
    # optimal)
    # The cell is highly sensitive to pH changes, slightly less sensitive to
    # temperature changes
    s_temp = 0.5
    s_ph = 2.0
    
    # The Synthetic Equation (Quadratic Penaly)
    # y = Max - c1(x1 - opt1)^2 - c2(x2 - opt2)^2
    titer = max_titer - (s_temp*(temp - opt_temp)**2) - (s_ph*(ph - opt_ph)**2)
    
    # Biology constraint: Titer can't be negative
    return max(0, titer)

# Test the synthetic bioreactor function
print(f'Titer at ideal conditions (37C, pH_7.2): {synthetic_bioreactor(37.0, 7.2)} g/L')
print(f'Titer at high temperature (39C, pH_7.2): {synthetic_bioreactor(39.0, 7.2)} g/L')
print(f'Titer at acidic conditions (37C, pH_6.8): {synthetic_bioreactor(37.0, 6.8)} g/L')