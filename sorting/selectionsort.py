# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:51:17 2020

@author: Shirlery
"""
"""
##> Selection Sort
    #==> This algorithm segements the list into two parts:
        #--> sorted
        #--> unsorted
    #==> We continuosly  remove the smallest element of the unsorted segment 
    # of the list and append it to the sorted segment

##> How it works
    #==> Note: No need to create a new list with the sorted elements, but we do treat
    # the leftmost part of the list as the sorted segement
    
    #==> We then search the entire list for the smallest element, and swao it with the
    # first element
    
    #==> Now, we know that the first element of the list is sorted. Then we get the smallest
    #element of the remaining items and swap it with the second element
    
    #==> This reiterates until the last item of the list is the remaining element to be examined

"""
##> Selection Sort Algorithm Implementation

def selectionSort(L):
    # Value of i corresponds to how many values were sorted
    for i in range(len(L)):
        #We assume that the first item is of the unsorted list is the smallest element
        minValue_index = i
        #This loop iterates over the unsorted list
        for j in range(i+1, len(L)):
            if L[j] < L[minValue_index]:
                minValue_index = j
        #swap the values of the lowest unsorted element with the first unsorted element
        L[i], L[minValue_index] = L[minValue_index], L[i]
    return L

#L = [12, 8, 3, 20, 11]
#selectionSort(L)
#print(L)

"""
    ##> Selection sort Properties
        #==> Space Complexity: O(n)
        #==> Time Complexity: O(n2)
        #==> Sorting in Place: Yes
        #==> Stable: No
"""           
        
    