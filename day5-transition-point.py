"""
(1) Problem
https://practice.geeksforgeeks.org/problems/find-transition-point-1587115620/1

(2) Example
	0 0 0 1 1
	3

(3) Idea

"""

"""
complete the function transitionPoint()
Your function should return transition index
"""


def transitionPoint(arr, n):
	length = len(lis)
	for index in range(length):
		item = lis[index]
		if item == 1:
			return index
	return -1

# O(n)
# binary search
