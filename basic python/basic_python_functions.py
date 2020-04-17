# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:25:59 2020

@author: Shirlery
"""

"""
def f(abc):
    statement_1
    statement_2
    ...
    return v

#==> Function name, arguments/parameters
#==> Body is indented
#==> Return statement exists and returnf a value

"""
##> Passing values to functions

#-> Argument value is substituted for name

def power(x,n):
    ans = 1
    for i in range(0, n):
        ans = ans*x
    return ans

#-> Like an implicit assgnment 

##> Another example

def update(l,i,v):
    if i >= 0 and i < len(l):
        l[i] = v
        return True #Not necessary
    else:
        v = v+1
        return False # Not necessary


##> Scope of names
    #==> Names within  a function have a local scope
    #==>

##> Recursive Functions
#==> A function that calls itself - recursion

def factorial(n):
    if n <= 0: # base case
        return 1
    else:
        return n*factorial(n-1)
    
##Prime numbers
#==> function to list orime numbers
#==> Prime number - only factors are 1 and itself
"""        
def isPrime(n):
    return factors(n) == [1,n]
"""
#--> 1 should not be reported as a prime
def factors(n):
    flist = []
    for i in range(1, n+1):
        if n%i == 0:
            flist = flist + [i]
    return flist

def isPrime(n):
    return factors(n) == [1,n]

def primesupto(n):
    primelist = []
    for i in range(1, n+1):
        if isPrime(i):
            primelist = primelist + [i]
    return primelist

#--> List the first n primes

def nprimes(n):
    (count, i, plist)= (0,1,[])
    while (count < n):
        if isPrime(i):
            (count, plist)= (count+1, plist+[i])
        i = i + 1
    return plist

##> for and while
#==> Can use while to simulate for
        