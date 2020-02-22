#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:09:20 2019

@author: clarkpain
"""


'''
Using bisection search to find more accurate minimum monthly pmt to pay off debt
'''
balance = 999999
reset = balance
annualInterest = .18
monthlyInterest = annualInterest / 12
bottom = balance/12
top = (balance + balance*((1+monthlyInterest)**12))/12
guess = (bottom + top)/12

while abs(balance) > .01: #checking to make sure there is a positive balance inputted
  balance = reset #resetting balance for calculation after previous iteration
  if balance > .01: #checking to see if guess is too small
    for month in range(0,12): #doing compound interest/payment calc for 12 mos
      balance = balance + (balance*monthlyInterest) - guess
    if balance > .01: #resetting bounds if payment too small
      bottom = guess
      guess = (bottom+top)/2
    elif balance < 0: #resetting bounds if payment too large
      top = guess
      guess = (bottom + top)/2
  elif .01 >= balance < 0:#checking to see if balance input is between 0 and .01
    print("You have a zero balance")
  elif balance < 0: #negative balance error
    print("Error1")
  else: #else Error
    print("Error2")
    
print(round(guess,2)) #rounding output to 2 decimal places