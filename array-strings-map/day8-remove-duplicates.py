"""
https://practice.geeksforgeeks.org/problems/remove-duplicates/0
"""

def remove_dups(string):
    lookup = set()
    ans = ''
    for char in string:
        if char not in lookup:
            lookup.add(char)
            ans += char
    return ans

if __name__ == '__main__':
    for _ in range(int(input())):
        string = input()
        print(remove_dups(string))
        