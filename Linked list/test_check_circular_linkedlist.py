# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:44:43 2020

@author: Shirlery
"""
from nose.tools import assert_equal

from check_circular_linkedlist import Node 

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextNode = b
b.nextNode = c
c.nextNode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextNode = y
y.nextNode = z


#############
class TestCycleCheck(object):
    
    def test(self,sol):
        assert_equal(sol(a),True)
        assert_equal(sol(x),False)
        
        print("ALL TEST CASES PASSED")
        
# Run Tests

t = TestCycleCheck()
t.test(Node.cycle_check)

