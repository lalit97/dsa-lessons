"""
https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0
"""

def reverse_words(string):
    string = string.split('.')
    ans = []
    for word in string[::-1]:
        ans.append(word)
    return '.'.join(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        string = input()
        ans = reverse_words(string)
        print(ans)