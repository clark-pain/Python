#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:52:10 2019

@author: clarkpain
"""

guess = 50
high = 100
low = 0

c = ""
l = ""
h = ""
choice = ""

print("Please think of a number between 0 and 100!")

while choice != "c":
    print("Is your secret number " + str(guess) + "?")
    choice = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if choice == "l":
        low = guess
        guess = int((guess + high)/2)
    elif choice == "h":
        high = guess
        guess = int((guess + low)/2)
    elif choice == "c":
        break
    else:
        print("Sorry, I did not understand your input.")


print("Game over. Your secret number was: ", + guess)
