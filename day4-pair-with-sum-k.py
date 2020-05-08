"""
(1) Problem
https://practice.geeksforgeeks.org/problems/key-pair/0

(2) Example

(3) Idea

"""

"""
complete the function key_pair()
return 'Yes' if pair with sum equal k exists
return 'No' othrewise
"""


def key_pair(lis, n, k):
	pass

if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split())
        lis = list(map(int, input().split()))
        ans = key_pair(lis, n, k)
        print(ans)