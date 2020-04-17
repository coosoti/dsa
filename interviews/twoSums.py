# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 08:02:19 2020

@author: Shirlery
"""


class Solution(object):
	def twoSum(self, nums, target):
		mapping = {}

		for index, val in enumerate(nums):
			diff = target - val
			if diff in mapping:
				return [index, mapping[diff]]
			else:
				mapping[val] = index