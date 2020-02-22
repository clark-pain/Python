#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:35:16 2019

@author: clarkpain
"""

def payoff(balance, annualInterestRate):
    '''
    Finding the lowest monthly payment to pay off loan in a year
    '''
    
    #Monthly interest rate = .05 / 12 = .0041666
    reset = balance
    payment = '' #minimum payment to keep up with interest
    pmt = 20
    
    while balance > 0:
        month = 0
        pmt = pmt + 10
        balance = reset
        while month < 12:
            balance = balance + (balance*(annualInterestRate/12)) - pmt
            month = month + 1
        
    
    print('Lowest Payment: ', round(pmt, 4))
    

        