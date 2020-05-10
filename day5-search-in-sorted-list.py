"""
(1) Problem 
https://practice.geeksforgeeks.org/problems/who-will-win/0

(3) Idea
Binary Search
"""

"""
def search(lis, n, k):
    length = len(lis)
    for i in range(length): #[0,1,2,3,4]
        item = lis[i]
        if item == k:
            return 1
    return -1

def search(lis, n, k):
    for item in lis:
        if item == k:
            return 1
    return -1
"""

def search(lis, n, k):
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high) // 2
        item = lis[mid]
        if item == k:
            return 1
        elif item < k:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split())
        lis = list(map(int, input().split()))
        ans = search(lis, n, k)
        print(ans)