#!/usr/bin/python3

import sys

def my_function():
    str = 'Hello World!'
    print (str)          # Prints complete string
    print (str[0])       # Prints first character of the string
    print (str[2:5])     # Prints characters starting from 3rd to 5th
    print (str[2:])      # Prints string starting from 3rd character
    print (str * 2)      # Prints string two times
    print (str + "TEST") # Prints concatenated string 

if __name__ == "__main__":
    my_function()
