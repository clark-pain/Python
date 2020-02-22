#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:46:31 2019

@author: clarkpain
"""

def debtCalc(balance, annualInterestRate, monthlyPaymentRate):
    '''
    amount left after a year under select conditions
    '''
    
   month = 0 
   while month < 12:
       balance = balance + (balance*(annualInterestRate/12)) - (balance*monthlyPaymentRate)
       month = month + 1
   else:
       print(round(balance, 2))