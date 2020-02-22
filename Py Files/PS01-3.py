#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:39:41 2019

@author: clarkpain
"""

s = 'azcbobobegghakl'

prevChar = ""
currentString = ""
longestString = ""

for char in s:
    if prevChar <= char:
        currentString += char
        if len(currentString) > len(longestString):
            longestString = currentString
    else:
        currentString = char
    prevChar = char
print('Longest substring in alphabetical order is: ' + longestString )