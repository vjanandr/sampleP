#!/usr/bin/python3

def my_list_function():
    list=[1,2,3,4]
    it = iter(list) # this builds an iterator object
    while True:
       print (next(it)) #prints next available element in iterator

if __name__ == "__main__":
     my_list_function()
