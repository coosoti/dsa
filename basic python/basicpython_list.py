# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 18:02:27 2020

@author: Shirlery
"""

#> List is a sequence of value
#==> Extract values by position, slice, like str
#==> Length is given by len()

#Lists and Strings
#==> For str, both a single position and a slice return strings
    #--> h = "hello"
    #--> h[0]==h[0:1] == "h"
    
#==> For lists, a single positiom returns a value, a slice returns a list
    #--> factors = [1,2,5,10]
    #--> factors[0]==1, factors[0:1]==[1]
## Nested lists
    #==> nested = [[2, [37]],4, ["hello"]]
    #--> nested[0] is [2, [37]]
    #--> etc.
## Updating lists
    #==> unlike strings, lists can be updated jn place 
    #==> Lists are mutable, unlike strings
    

##> Mutable vs immutable
    #==> For immutable values, we can assume that assignment makes a fresh
    #copy of the value --> int, float, bool str ==> immutable
    
    #==> For mutable values, assign,ent foes not make a fresh copy
    
## Copying lists
    #==> How can we make a copy of a list?
    #==> A slice creates a new sub(list) from an old one
    #==> To make a copy of a list, use a full slice
        #--> eg. list2 = list[:]