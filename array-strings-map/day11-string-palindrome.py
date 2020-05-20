"""
https://practice.geeksforgeeks.org/problems/palindrome-string/0
"""

"""
return `Yes` or `No`
"""
def is_palindrome(string, length):
    # ans = []
    # for char in string[::-1]:
    #     ans.append(char)
    # ans = ''.join(ans)

    if string == string[::-1]:
        return 'Yes'
    else:
        return 'No'

def is_palindrome(string, length):
    # O(n/2)
    start = 0
    end = length - 1
    while end > start:
        if string[start] != string[end]:
            return 'No'
        start += 1
        end -= 1
    return 'Yes'


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        string = input()
        ans = is_palindrome(string, n)
        print(ans)