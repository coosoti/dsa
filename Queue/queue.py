# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 07:42:55 2020

@author: Shirlery
"""

"""
enqueue() - add item to end of queue - O(1)
dequeue() - remove item - O(1)
peek() - return item
FIFO strcture
"""

class Queue:
    
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return self.queue == []
    
    def enqueue(self, data):
        self.queue.append(data)
        
    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def peek(self):
        return self.queue[0]
    
    def sizeQueue(self):
        return len(self.queue)


#queue = Queue()

#queue.enqueue(10)
#queue.enqueue(20)
#queue.enqueue(30)
#queue.enqueue(40)
#print(queue.sizeQueue())

#print("Dequeue: ", queue.dequeue())
#print("Dequeue: ", queue.dequeue())

#print(queue.sizeQueue())