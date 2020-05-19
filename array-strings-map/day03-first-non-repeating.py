"""
(1) Problem
https://practice.geeksforgeeks.org/problems/non-repeating-character/0

(2) Example
    string: lhello
    answe: h
(3) Idea
    1. count characters
    2. and then loop through the string
    and print the first charcter which has 
    count 1
"""

"""
complete the function non_repeat()
return the first non repeating character
"""

def get_counter(string):
    counter = {}
    for char in string:
        if char not in counter:
            counter[char] = 1
        else:
            counter[char] += 1
    return counter


def non_repeat(string, n):
    counter = get_counter(string)
    for char in string:
        if counter[char] == 1:
            return char
    return -1


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        string = input()
        ans = non_repeat(string, n)
        print(ans)