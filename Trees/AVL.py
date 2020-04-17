# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 08:22:23 2020

@author: Shirlery
"""
"""
Balance Binary Tree: AVL trees or red-black trees. They are guaranteed
to be balance ==> thus, O(logN) is guaranteed
==> Are predictable
==> For example:
    Construct a BST from a sorted array
    ==> [1,2,3,4] ==> This will result into a linked list reducing 
                     time complexity to O(N)

"""
class Node:
    
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None

class AVL:
    
    def __init__(self):
        self.root = None
        
    
    def insert(self, data):
        self.root = self.insertNode(data, self.root)
    
    def insertNode(self, data, node):
        if not node:
            return Node(data)
        
        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)
        
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild) + 1)
        
        return self.settleViolations(data, node)
    
    def settleViolations(self, data, node):
        
        balance = self.calcBalance(node)
        
        # case 1: --> left left heavy situation
        if balance > 1 and data < node.leftChild.data:
            print("Left left heavy situation...")
            return self.rotateRight(node)
        
        # case 2: --> Right right heavy situation
        if balance < -1 and data > node.rightChild.data:
            print("Right right heavy situation...")
            return self.rotateLeft(node)
        
        if balance > 1 and data > node.leftChild.data:
            print("Left right heavy situatiom...")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)
        
        if balance < -1 and data < node.rightChild.data:
            print("Right left heavy situation ...")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)
        
        return node
        
        
    def calcHeight(self, node):
        
        if not node:
            return -1
        
        return node.height
    
    # if it return value > 1 it is a left heavy tree - make right rotation
    #otherwise if value < -1 right heavy tree --> left rotation
    def calcBalance(self, node):
        
        if not node:
            return 0
        
        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)
    
    def traverse(self):
        if self.root:
            self.traverseInorder(self.root)
    
    def traverseInorder(self, node):
        
        if node.leftChild:
            self.traverseInorder(node.leftChild)
        
        print("%s " % node.data)
        
        if node.rightChild:
            self.traverseInorder(node.rightChild)
    
    def rotateRight(self, node):
        print("Rotating to the right of node ", node.data)
        
        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild
        
        tempLeftChild.rightChild = node
        node.leftChild = t
        
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightchild) + 1)
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightchild) + 1)
        
        return tempLeftChild
    
    def rotateLeft(self, node):
        print("Rotating to the left of node ", node.data)
        
        tempRightChild = node.rightChild
        t = tempRightChild.leftChild
        
        tempRightChild.leftChild = node
        node.rightChild = t
        
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightchild) + 1)
        tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightchild) + 1)
        
        return tempRightChild
    
    
avl = AVL()

avl.insert(5)
avl.insert(2)
avl.insert(7)
avl.insert(6)
avl.insert(8)
avl.traverse()