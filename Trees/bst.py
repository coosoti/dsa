# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:56:24 2020

@author: Shirlery
"""
"""
##Trees - We have nodes with the data and connection between the
 nodes // edges
 
##root node: We have a reference to this, all other nodes can be accessed 
 via the root node

##Definitions 
 A node directly connected to another node --> child
 The opposite --> parent node
 Leaf nodes: nodes with no children
 
 Binary Search Tree 
 ===================
 -- every node can have atmost two children: left and right child
 -- left child: smaller than the parent
 -- right child: greater than the parent
 
 Why BST is good??
 On every decision, e get rid of half of the data in which we are searching
 // like binary search
 -- O(log N) time complexity
 
 Height of the tree, h: the number of layers it contains ==> the length of
 of the path from the root to the deepest node in the tree ==> We should
 keep the height of the tree at a minimum which is h=log n
 In general,
 h ~ O(log N) ==> if this is true, the tree is said to be balanced. ==>
 If it is not true, the tree is unbalanced, which means it is asymetric, 
 which is a problem ==> the running time is no more logarithmic h=log n // no-
 longer valid
 
 BST - operations
 ==================
 
 Insertion: We start at the root node. if the data we want to insert is greater
 is greater than the root node, we go to the right. If it is smaller,
 we go to the left... snd so on...
 
 Search: We start at the root node. If the data we want to find is gre
 ater than the root node, we go to the right. if it is smaller, we go
 to the left node until we find it.
 
 ## If we want to find the smallest node, we have to go to the left as
 far as possible==> it will be the smallest
 ## If we want to find the largest node, we have to go to the right as
 far as possible==> it will be the largest
 
 Delete: soft delete --> we do not remove the node from the BST, we 
 just mark it that it has been removed - not so efficient
 
 The possible cases:
     i) get rid of a leaf node: -- search and set it to null
     ==> complexity: we have to find the item, then delete it or set it 
     to NULL ~~ O(log N) find operation + O(1) deletion= O(log N)
     
     ii) Getting rid of a node with a single child: - we update the
     references
     ==> complexity: we find the item and we update the references
     ~~ set the parent's pointer points to its grandchild directly
     ~~ O(log N) find operation + O(1) update references = O(logN)
    
     iii) Getting rid of a node with two children: 
      Options:
          1. We look for the largest item in the left subtree 
             ==> predecessor
          2. the smallest item in the right subtree
             ==> successor
        ===> We look for the predecessor and swap the two nodes
                 --> we end up at a case:
                     I. situation -as leaf node: we ust set it to NULL
        ===> We look for the successor and swap the two nodes
                 --> we end up with case:
                     II. situation - with a single child: we just have
                     to update the references
        ==> Complexity: O(logN)

 Traversal: Visiting every node in the tree;
 
 The possible ways:
     i) In-order traversal: we visit the left subtree + the root node
    + the right subtree recursively
     ii) Pre-order traversal: we visit the root node + left subtree +
    the right subtree recursively
     iii) Post-order traversal: We visit the left subtree + right sub
    tree + the root recursively

                Average Case       Worst Case
Space/memory    O(n)               O(n)
Insert          O(log n)           O(n)
Delete          O(log n)           O(n)
Search          O(log n)           O(n)

Worst Case Scenarios:
--> if the tree becomes unbalanced, the operations' running times can
be reduced to O(N) in the worst case
--> therefore it is important to keep the tree as balanced as possible                    
 """

# creating a class Node 
class Node:
    
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
 
class BinarySearchTree:
    
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)
    
    # O(logN) if the tree is balanced otherwise ==> O(N)
    def insertNode(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)
    
    def removeNode(self, data, node):
        if not node:
            return node
        
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node...")
                del node
                return None
            
            if not node.leftChild:
                print("Removing a node with a single right child...")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print("Removing a node withf a single left child...")
                tempNode = node.leftChild
                del node
                return tempNode
            print("Removing node with two children...")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)
            
        return node
            
    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        
        return node
    
    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)
            
    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)
        
    def getMin(self, node):
        
        if node.leftChild:
            return self.getMin(node.leftChild)
        
        return node.data
    
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)
    
    def getMax(self, node):
        
        if node.rightChild:
            return self.getMax(node.rightChild)
        
        return node.data
    
    def traverse(self):
        
        if self.root:
            self.traverseInOrder(self.root)
    
    def traverseInOrder(self, node):
        
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
            
        print("%s " % node.data)
        
        if node.rightChild:
            self.traverseInOrder(node.rightChild)


#Testing
#bst = BinarySearchTree()

#insertion

#bst.insert(10)
#bst.insert(5)
#bst.insert(15)
#bst.insert(6)

#print(bst.getMinValue())
#print(bst.getMaxValue())
#bst.traverse()
        

            
        
            
                
        























       