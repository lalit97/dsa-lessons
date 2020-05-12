"""
https://practice.geeksforgeeks.org/problems/missing-number-in-array/0
"""




def missing_number(lis, n): # 5 # 1 2 3 5
	total = (n) * (n + 1) // 2
	s = sum(lis)
	return total - s


if __name__ == '__main__':
	t = int(input())
	for i in range(t):
		n = int(input())
		lis = list(map(int, input().split()))
		ans = missing_number(lis, n)
		print(ans)

