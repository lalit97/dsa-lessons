"""
(1) Problem
https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array/0

Constraints:
1 <= T <= 100
1 <= N <= 1000
1 <= A[i] <= 10^12

(2) Example
	arr = [1,3,5,6,13]
	ans = min = 1, max = 13

(3) Idea 
	just iterate through loop 
	and get min and max
"""

"""
complete the function minmax()
return minimum and maximum from array
"""

def minmax(arr, n):
	max = 0
	min = 10**12
	for item in arr:
		if item > max:
			max = item
		if item < min:
			min = item
	return (min, max)


if __name__ == '__main__':
	for _ in range(int(input())):
		n  = int(input())
		arr = list(map(int, input().split()))
		min, max = minmax(arr, n)
		print(min, max)