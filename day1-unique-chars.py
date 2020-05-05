"""
(1) Problem (CTCI): 
Is Unique: Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?

(2) example
# string = "hellowrold"
# string2 = "abcd"

# char_count = {'h':2, 'e':1, 'l':1, 'o':1}


(3) Idea
1. loop through the string
2. count frequency of each charcter
"""

def unique_chars(string):
	char_count = {}
	for char in string:  
		if char not in char_count:
			char_count[char] = 1
		else:
			return False
	return True


if __name__ == '__main__':
	string = input()
	ans = unique_chars(string)
	print(ans)
