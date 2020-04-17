# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 06:53:53 2020

@author: Shirlery
"""

# Euclid's Algorithm
# ========================
# Suppose d divides both m and n, and m > n
# then m = ad, n = bd
# so m-n = ad - bd = (a-b)d
# d divided m-n as well
# so gcd(m,n) = gcd(n, m-n)

#First Illustration of Euclid's algorithm
#---------------------------------------#

# Consoder gcd(m,n) with m > n
# If n divides m, return n
# Otherwise, compute gcd(n, m-n) and return that value

def gcd_version1(m,n):
    # Assume m >= n
    if m < n:
        (m,n) = (n,m)
        
    if m%n == 0:
        return n
    else:
        diff = m-n
        # diff > n? Possible!
        return gcd_version1(max(n, diff), min(n,diff))
    

def gcd_version2(m,n):
    if m < n: #Assume m >= n
        (m,n) = (n,m)
        
    while (m % n) != 0:
        diff = m - n
        # diff > n? Possible!
        (m,n) = (max(n, diff), min(n,diff))
    return n

# Second Illustration of Euclid's algorithm ==> Actual Euclid's Algo
#=========================================
    
# Suppose n does not divide m
# Then m = qn + r, where q is the quotient, r is the remainder when
# we divide m by n
# Assume d divided both m and n
# Then  m = ad, n = bd
# So ad = q(bd) + r
# It follows that r = cd, so d divides r as well


# Implementation of actual Euclid's Algorithm
#=============================================
    
# Consider gcd(m,n) with m > n
# if n divides m, return n
# Otherwise, let r = m%n
# Return gcd(n,r)

def gcd(m,n):
    
    if m < n: # Assume m >= n
        (m,n) = (n,m)
        
    if (m%n) == 0:
        return n
    else:
        return gcd(n, m%n) # m%n < n always!

def gcd_v2(m,n):
    
    if m < n: #Assume m >= n
        (m,n) = (n,m)
    
    while (m%n) != 0:
        (m,n) = (n, m%n) # m%n < n always
        
    return n