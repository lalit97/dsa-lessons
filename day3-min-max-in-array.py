"""
(1) Problem
https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array/0

(2) Example

(3) Idea 
"""

"""
complete the function minmax()
return minimum and maximum from array
"""

def minmax(arr, n):
	pass

if __name__ == '__main__':
	for _ in range(int(input())):
		n  = int(input())
		arr = list(map(int, input().split()))
		min, max = minmax(arr, n)
		print(min, max)