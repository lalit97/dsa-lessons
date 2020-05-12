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
"""
def transitionPoint(arr, n):
	length = len(lis)
	for index in range(length):
		item = lis[index]
		if item == 1:
			return index
	return -1

"""
def transitionPoint(arr, n):  # 0 0 0 0 0 0 0 1 1 1 1
	low = 0
	high = n-1
	if arr[0] == 1:
		return 0
	while low <= high:
		mid = (low + high) // 2
		if arr[mid] == 1:
			if arr[mid-1] == 0:
				return mid
			high = mid-1
		elif arr[mid] == 0:
			if mid + 1 < n and arr[mid+1] == 1:
				return mid + 1
			low = mid + 1
	return -1	
