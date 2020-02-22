#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 08:35:28 2019

@author: clarkpain
"""

def polysum(n, s):
    import math
    return round(((0.25*n*(s**2))/(math.tan(math.pi/n))) + ((n*s)**2), 4)