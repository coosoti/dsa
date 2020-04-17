# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:34:51 2020

@author: Shirlery
"""

#> Manipulating Text
###> computation is a lot more than number crunching
###> Text processing is increasingly important
    #==> Document preparation
    #==> Importing/Exporting Spreadsheet data
    #==> Matching search queries to content

###> String - type str
    #==> str is sequence of characters
    #==> Enclose in quotes - single, double, triple

##> Strings as sequence
    #==> Positions 0,1,2,...,n-1 for a string of length n forward
    #==> Positions -1,-2,-3, ... count backwards from the ned

##> Operations  on strings
    #==> Combine two strings: Vonvatenatin, operator +
    #==> len(s) return length of string s
##> Extracting substring
    #==> A slice is a "segment of a string
        #=-> s[1:] etc
##> Modifying strings
    #==> Cannot update a string "in place"
    #==> Instead, use slices and concatenation
        #--> s = s[0:3] + "p!"
    ##>>> Strings are immutable objects
        