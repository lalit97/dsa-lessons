"""
(1) Problem
https://practice.geeksforgeeks.org/problems/anagram/0

(2) Example

string1: hello
dict1: {'h':1, 'e':1, 'l':2, 'o':1}

string2: ollsh
dict2: {'o':1, 'l':2, 'e':0, 'h':1}   

(3) Idea -> the characters and their count should be same
so we can build a frequency array/counter
"""


def get_counter(string):
    counter = {}
    for char in string:
        if char not in counter:
            counter[char] = 1
        else:
            counter[char] += 1
    return counter


def is_anagram(string1, string2):
    dict1 = get_counter(string1) 
    dict2 = get_counter(string2)   
    
    for alphabet in "abcdefghijklmnopqrstuvwxyz":
        if dict1.get(alphabet) != dict2.get(alphabet):
            return "NO"
    return "YES"


if __name__ == '__main__':
    for _ in range(int(input())):
        string1, string2 = input().split()
        ans = is_anagram(string1, string2)
        print(ans)