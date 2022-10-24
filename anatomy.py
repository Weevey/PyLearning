#!/usr/bin/python
# imports sys module
import sys
# Define variable argc as the count of values in sys.argv array
# Sys.argv appears to contain file path for current file(anatomy.py)
argc = len(sys.argv)
# Check if argc is bigger than one, if it is print statement
if argc > 1:
    print('Too may args')
# If argc is not bigger than 1, execute following code
else:
    # Define variable where as "World"
    where = 'World'
    # Print concatenation of string "Hello" and variable where
    print("Hello", where)
# Print concatenation of "Goodbye from" and value of sys.argv array position 0
print('Goodbye from ' +
      sys.argv[0])
