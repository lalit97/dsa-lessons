"""
https://practice.geeksforgeeks.org/problems/multiply-left-and-right-array-sum/0
"""

def left_right_sum(lis, n):
	pass

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        lis = list(map(int, input().split()))
        ans = left_right_sum(lis, n)
        print(ans)
