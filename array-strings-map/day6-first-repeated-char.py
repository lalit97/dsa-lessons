"""
https://practice.geeksforgeeks.org/problems/find-first-repeated-character/0
"""


def first_repeat(string): 
    counter = {}
    for char in string:
        if char not in counter:
            counter[char] = 1    # {'a':1, 'b':1, 'c':1}
        else: 
            return char
    return -1


def first_repeat(string): 
    lookup = set()
    for char in string:
        if char not in lookup:
            lookup.add(char)        # {'a', 'b', 'c'}
        else: 
            return char
    return -1

if __name__ == '__main__':
    for _ in range(int(input())):
        string = input()
        ans = first_repeat(string)
        print(ans)
