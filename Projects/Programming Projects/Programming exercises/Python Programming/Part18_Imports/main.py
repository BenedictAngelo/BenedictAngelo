# module = a file containing code you want to include in your program
#           use 'import' to include a module (built-in or your own)
#           useful in break up large program reusable separate files

# this is the better way
import math 

print(math.pi)

#import math as m
#print(m.pi)


# from math import e ##exponential
# a = 2
#print(e ** a)

# creating a module for other files to use
pi = math.pi

def square(x):
    return x ** 2

def circumference(radius):
    return 2 * pi * radius
