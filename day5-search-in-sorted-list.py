"""
(1) Problem 
https://practice.geeksforgeeks.org/problems/who-will-win/0

(2) Example

(3) Idea
"""




def search(lis, n, k):
	pass



if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split())
        lis = list(map(int, input().split()))
        ans = search(lis, n, k)
        print(ans)