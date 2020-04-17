# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 21:44:06 2020

@author: Shirlery
"""
## Control Flow

#==> Function definitions are 'digested' for future use
#==> Control flow determines order in which statements are executed
    #--> Conditional execution
    #--> Repeated execution - loops
    #--> Function definitions

##> Conditional Execution, if:
    #==> 
##> Multiway branching, elif:

##> Loops: repeated actions

###> Find alll factors of a number n
###> Factors must lie between 1 and n
def factors(n):
    flist = []
    for i in range(1, n+1):
        if n%i == 0:
            flist = flist + [i]
    return flist

#===> Can alter the control flow using 
    #--> if .. elif .. else
    #--> range for ...
    #--> while loop