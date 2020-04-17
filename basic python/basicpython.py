# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:05:59 2020

@author: Shirlery
"""

#Assign statement
##> Assign a value to a name
i = 5
j = 2*i
j = j + 5

##> Left hand side is a name
##> Right hand side is an expression
    #==> Operations in expression depend on the type of value

###> Numerical Values
    #==> int --> integers
    #==> float --> fractional numbers 
    
#> int vs float
    #==> internally a value is stored as a finite sequence of 0s and 1s(bits)
    #==> For int, this sequence is read off as a binary number
    #==> For float, this sequence breaks up into a mantissa and exponent
        #-------> Like scientific notation: 0.602X10^24 

#> Opreations on numbers
    #==> +, -, *, /
    #==> / always produces a float
    #==> Quotient and remainer: // and %
    #--> 9//5 is 1, 9%5 is 4
    #==> Exponentiation: **
    #--> 3**2 is 9

###> Boolean Values: bool
    #==> True, False

##> Example

def divides(m,n):
    if n%m == 0:
        return True
    else:
        return False

def even(n):
    return(divides(2,n))

def odd(n):
    return(not divides(2,n))