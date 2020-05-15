"""
(1) Problem
https://practice.geeksforgeeks.org/problems/key-pair/0

(2) Example
[1, 2, 3, 4], k = 7

(3) Idea
a) Brute-Force just iterate through list and check
b) Sorting + 2 pointer technique
c) Create a lookup and solve
"""

"""
complete the function key_pair()
return 'Yes' if pair with sum equal k exists
return 'No' othrewise
"""

"""
def key_pair(lis, n, k):
    length = len(lis)
    for i in range(length):
        for j in range(i+1, length):
            curr_sum = lis[i] + lis[j]
            print(lis[i], lis[j])
            if curr_sum == k:
                return 'Yes'
    return 'No'


def key_pair(lis, n, k):
    # 2 pointer technique
    # input -> [2, 3, 1 ,4]
    # sorted -> [1, 2, 3, 4] #nlogn K = 4

    sorted_lis = sorted(lis)
    left = 0
    right = n-1
    while right > left:
        sum = lis[left] + lis[right]
        if sum == k:
            return 'Yes'
        if sum > k:
            right -= 1
        else:
            left += 1
    return 'No'
"""

def key_pair(lis, n, k):
    lookup = set()           #{1, 5, 4, 3, 7}
    # [1,4,5,3,6] search O(n) time
    # {1,4,5,3,6} search O(1) time 
    # k = 8
    for item in lis:
        if k-item in lookup:
            return 'Yes'
        lookup.add(item)    #{1, 4, 5, }
    return 'No'


if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split())
        lis = list(map(int, input().split()))
        ans = key_pair(lis, n, k)
        print(ans)