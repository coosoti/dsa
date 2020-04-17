# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:42:14 2020

@author: Shirlery
"""

##> List functions & syntax
#==> list1.append(v) --> extend a list by a single value
#==> list1.extend(list2) --> extends a list by another list of values
#==> list1.remove(x) --> removes the first occurence of x

##> List memberships

#==> xin l returns True if value x is found in list x

#==> l.reverse() --> reverse l in place
#==> l.sort() --> sort l in ascending order
#==> l.index(x) --> find leftmost position of x in l
    #--> avoid error by checking if x in l
#==> l.rindex(x) --> find the rightmost position of x in l

##>Search for a value in a list
##===================================
"""
def findpos(l,v):
    # Return first position of v in l
    # Return -1 if v not in l
    (found, i) = (False, 0)
    while i < len(l):
        if not found and l[i] == v:
            (found, pos) = (True, i)
    if not found:
        pos = -1
    return pos
"""

def findpos(l, v):
    (pos, i) = (-1, 0)
    for x in l:
        if x == v:
            pos = i
            break
        i = i + 1
    # If pos not present in loop, pos is -1
    return pos

def findpos_v2(l,v):
    pos = -1
    for i in range(len(l)):
        if l[i] == v: # Exit, report positiom
            pos = i
            break
        else:
            pos = -1 # No break, v not in l
    return pos