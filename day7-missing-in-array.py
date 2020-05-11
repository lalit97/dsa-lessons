"""
https://practice.geeksforgeeks.org/problems/missing-number-in-array/0
"""





def missing_number(lis, n):
	pass

if __name__ == '__main__':
	t = int(input())
	for i in range(t):
		n = int(input())
		lis = list(map(int, input().split()))
		ans = missing_number(lis, n)
		print(ans)

