#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 07:26:55 2019

@author: clarkpain
"""

def isin(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    Recursive search
    '''
    if aStr == '':
        return False

    testchar = aStr[(len(aStr))//2]
    
    if char == testchar:
        return True
    elif len(aStr) == 1:
        return False
    else:
        if char < testchar:
           return isin(char, aStr[:len(aStr) // 2])
        elif char > testchar:
           return isin(char, aStr[(len(aStr) // 2):])
    return isin(char, aStr)