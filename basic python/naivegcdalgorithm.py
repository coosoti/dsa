# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 05:55:57 2020

@author: Shirlery
"""
#A naive algorithm for gcd(m,n)
#==============================================================
# Use fm, fn for the list of factors of m, n, respectively
# For each i from 1 to m, add i to fm if i divides m
# For each j from 1 to n, add j to fn if j divides n
# Use cf for a list of common factors
# For each f in fm, add f to cf if f also appears in fn
# Return largest(rightmost) value in cf

#Implementation

def gcd(m, n):
    fm = []
    for i in range(1, m+1):
        if (m % i) == 0:
            fm.append(i)
    
    fn = []
    for j in range(1, m+1):
        if n % j == 0:
            fn.append(j)
    
    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)
    
    return (cf[-1])