# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 09:58:22 2020

@author: Shirlery
"""
## Example 
##==> Sort the list [3,2,4,1] using bubble sort

#--> How it works
#1 Start by comparing the first two items on the list i.e. 3 and 2
    #--> 2 is smaller than 3, therefore they swap places
       #--> thus, 2,3,4,1 ==> updated list
#2 Next, compare the third item with the second item of the updated list i.e. 3 and 4
    #--> 3 is smaller than 4 so you do not wap
        #--> thus, 2,3,4,1 ==> updated list
#3 Next, you compare the fourth item with the updated third i.e. 1 and 4
    #--> 1 is smaller than 4, therefore they swap places
        #--> thus, 2,3,1,4, updated list

#4 Next, we start at the beginning and repeat steps 1 to 3 until the list is sorted

##> Implementation:
        # Outer loop: We use loop variable i, i = 0 to i = n-1
        # Inner loop: We use loop variable j, j = 0 to n-1-i => because we know 
                     # the last item on thelist is already sorted

def bubbleSort(L):
    for i in range(0, len(L)-1): #O(n)
        for j in range(0, len(L) - 1 - i): #O(n)
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L

# time complexity ==> O(n^2)
# space complexity ==> O(1)