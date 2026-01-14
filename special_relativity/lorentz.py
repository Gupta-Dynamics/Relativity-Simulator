# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 11:36:00 2026

@author: ag261
"""

import numpy as np

def gamma(v, c=1):
    return 1 / np.sqrt(1 - (v/c)**2)

def lorentz_transform(t, x, v, c=1):
    g = gamma(v, c)
    t_p = g * (t - v * x / c**2)
    x_p = g * (x - v * t)
    return t_p, x_p

def inverse_lorentz(t_p, x_p, v, c=1):
    g = gamma(v, c)
    t = g * (t_p + v * x_p / c**2)
    x = g * (x_p + v * t_p)
    return t, x
