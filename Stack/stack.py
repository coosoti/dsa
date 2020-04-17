# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 21:48:09 2020

@author: Shirlery
"""
"""
ADT
===========
LIFO - Last In First Out
operations
pop() - Removing items - O(1)
push() - Adding items - O(1)
peek() - Return the top most items but does not remove

"""
## Implementation of Stacks with list

class Stack:
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return self.stack == []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    def peek(self):
        return self.stack[-1]
    
    def sizeStack(self):
        return len(self.stack)
    

#Testing
#stack = Stack()
#stack.push(1)
#stack.push(2)
#stack.push(3)        
        
#print(stack.sizeStack())
#print("Popped: ", stack.pop())
#print("Popped: ", stack.pop())
#print(stack.sizeStack())
        
#print(stack.sizeStack())