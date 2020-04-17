# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 18:18:29 2020

@author: Shirlery
"""
"""


## Linkedlist

#A linkedlist is a data structure that consists of many mini-data structures 
called 'Nodes'.

#The nodes link together to form a list.

# Each node has two attributes

# 1 - Value/data  - can contain anything - int, str, objects etc.
# 2 - A pointer to the next node in the sequence

## PS
#### Head Node ===> The first node in the linkedlist
#### Tail Node ===> Is the last node in the sequence
"""

## Here we created a class that has a value and nextNode attribute
class Node:
	def __init__(self, value):
		self.value = value
		self.nextNode = None

## For example, we create 3 individual nodes
#node1 = Node("3") # "3"
#node2 = Node("7") # "7"
#node3 = Node("10") # "10"

## The next step is to connect the three nodes together
# node1.nextNode = node2 
# node2.nextNode = node3 

# The first line above makes node1 point to node2
# "3" --> "7"
# The second line above makes node2 point to node3
# "7" --> "10"

###==> All together, we have a linkedlist that looks like this
# "3" --> "7" --> "10" --> Null

#Note ==> node3 ("10")points to null, because there is no nextNode assigned to 
#node3, and the default to nextNode is Null
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    # O(1)
    def insertStart(self, value):
        self.size = self.size + 1
        newNode = Node(value)
        
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
            
    def remove(self, value):
        if self.head is None:
            return
        self.size = self.size - 1
        
        currentNode = self.head
        previousNode = None
        
        while currentNode.value != value:
            previousNode = currentNode
            currentNode = currentNode.nextNode
        
        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode
    # O(1)        
    def size1(self):
        return self.size
    
    # O(N) Not Good
    def size2(self):
        actualNode = self.head
        size = 0
        
        while actualNode is not None:
            size = size + 1
            actualNode = actualNode.nextNode
        
        return size
    
    # O(N)
    def insertEnd(self, value):
        
        self.size = self.size + 1
        newNode = Node(value)
        actualNode = self.head
        
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        
        actualNode.nextNode = newNode
    
    
    def traverseList(self):
        
        actualNode = self.head
        
        while actualNode is not None:
            print("%d " %actualNode.value)
            actualNode = actualNode.nextNode
        
"""        
Testing the LinkedList   
""" 
#Creating a linklist
#linkedlist = LinkedList()

#linkedlist.insertStart(0)
#linkedlist.insertStart(5)
#linkedlist.insertStart(10)
#linkedlist.insertStart(15)
#linkedlist.insertEnd(100)

#traverseList
#linkedlist.traverseList()

#size
#linkedlist.size1()

#remove
#linkedlist.remove(0)
#linkedlist.remove(5)
#linkedlist.remove(10)
#linkedlist.remove(15)
#linkedlist.remove(100)    








