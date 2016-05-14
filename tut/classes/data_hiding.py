#!/usr/bin/python3

class JustCounter:
   __secretCount = 0 # Underscore the variable to hide

   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print (counter._JustCounter__secretCount) # works fine
print (counter.__secretCount) # Exception

