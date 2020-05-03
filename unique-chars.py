"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
"""

# example
# string = "hellowrold"
# string2 = "abcd"
"""
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
	
	# # print(char_count)
	# # print(char_count.keys())
	# # print(char_count.values())
	# for val in char_count.values(): #[1, 1, 1, 1]
	# 	if val != 1:
	# 		return "False"
	# return "True"
	
# char_count = {'h':2, 'e':1, 'l':1, 'o':1}

if __name__ == '__main__':
	string = input()
	ans = unique_chars(string)
	print(ans)
