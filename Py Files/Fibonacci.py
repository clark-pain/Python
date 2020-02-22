#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 19:37:17 2019

@author: clarkpain
"""

def fib(x):
    '''
    returns fibonacci of x
    '''
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


def ispalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))
