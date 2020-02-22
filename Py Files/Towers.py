#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:36:07 2019

@author: clarkpain
"""

def printMove(fr,to):
    print('move from' + str(fr) + 'to' + str(to))
    
def towers(n, fr, to, spare):
    if n == 1:
        printMove(fr,to)
    
    else:
        towers(n-1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n-1, spare, to, fr)
        

def gcdIter(a,b):
    '''
    greatest common denominator for 2 integers using iterations
    '''
    testvalue = min(a,b)
    while a % testvalue != 0 or b % testvalue != 0:
        testvalue -= 1
    return testvalue


def gcdRecur(a,b):
    '''
    greates common denominator for 2 integers using recursion
    '''
    
    testvalue = min(a,b)
    if a % testvalue != 0 or b % testvalue != 0 :
        testvalue -= 1
    else:
        return testvalue 
    
def gcdRecur2(a,b):
    if b == 0:
        return a
    else:
        return gcdRecur2(b, a%b)
        
        
            