"""
https://practice.geeksforgeeks.org/problems/anagram/0
"""




"""
Your task is to complete the function 
"is_anagram()"

return "YES" if strings are anagram
return "NO" if not.
"""

def is_anagram(string1, string2):
	


if __name__ == '__main__':
    for _ in range(int(input())):
        string1, string2 = input().split()
        ans = is_anagram(string1, string2)
        print(ans)