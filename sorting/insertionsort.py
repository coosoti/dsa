# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 10:44:56 2020

@author: Shirlery
"""
# Example
#--> Sort the list [7,8,5,4,9,2] using insertion sort algorithm

## How it works
# Start with a single item in our sorted list on the left, i.e. 7 and one
  # by one we are going to work through the unsorted list i.efrom 8 to 2 
  # and move each item into its correct position
# We know that the first item, 7, is already sorted if it's only one item
  # in the list
# Next we are looking at the second item i.e. 8, is 8 greater than 7? Yes,
  # then it is the correct position.
  #--> We mark 8 as sorted --> [7,8,5,4,9,2]
#Next, we look at the third item i.e. 5, is it greater than 8? No, then
  # we swap it with 8 --> [7,5,8,4,9,2] 
  # and is it greater than 7? No we swap it with 7 --> [5,7,8,4,9,2]
# We repeat the process until the list is sorted.

# Implementation Test
# Basic
"""
def insertionSort(L):
    for i in range(1, len(L)): # starting from the 2nd item on the list
        for j in range(i - 1, 0, -1): # starting from immediate left of i and walk our way to 0
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
            else:
                break


def insertionSortv2(L):
    for i in range(1, len(L)):
        j = i-1
        while L[j] > L[j+1] and j >= 0:
            L[j], L[j + 1] = L[j + 1], L[j]
            j -= 1

#Note: the expensive operation is swapping
          


def insertionSort(L):
    for i in range(1, len(L)):
        curNum = L[i]
        for j in range(i-1, 0, -1):
            if L[j] > curNum:
                L[j+1] = L[j]
            else:
                L[j+1] = curNum
        break
    return L
            

""" 
#optimized insertion algorithm
# This is preferred because you avoid  swapping the items

def insertionSort(L):
    # start at the second element as we assune that the first element is sorted
    for i in range(1, len(L)):
        curNum = L[i] # curNum is the item we are looking to insert into it's correct place
        j = i - 1 # j is the reference of the index of the previous item
        
        #Move all the items on the sorted part to the right if they are larger than curNum
        while j >= 0 and L[j] > curNum:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = curNum
    return L

"""
##> Note
    #==> in-place: Requires a small, constant additional space (no matter the input size of 
    the collection), but rewrites the original memory locations of the elements in the 
    collection.
    #==> stable: The algorithm maintains the relative order of equal objects from the initial 
    array. In other words, say your company's employee database returns "Dave Watson" and 
    "Dave Brown" as two employees, in that specific order. If you were to sort them by their (shared) 
    first name, a stable algorithm would guarantee that this order remains unchanged.

##> Properties of Insertion Sort
    #==> Space Complexity: O(1)
    #==> Time Complexity: O(n), O(n* n), O(n* n) for Best, Average, Worst cases respectively.
    #==> Sorting In Place: Yes
    #==> Stable: Yes
        
        
       