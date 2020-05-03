'''
https://practice.geeksforgeeks.org/problems/uncommon-characters/0
'''
'''
sorting fails 

characters
c == a
h == a
a == a

26 * (n1 + n2)
'''
import string

# def uncom_char(string1, string2):
# 	for char in string.ascii_lowercase:
# 		for char1 in string1:
# 			if char == char1:
# 				break 
# 		for char2 in string2:
# 			if char == char2:
# 				break 
		
# 		if found in both:
# 			don't print
# 		else:
# 			print 
			

def uncom_char(string1, string2):
	str_set1 = set(string1)
	str_set2 = set(string2)
	for char in string.ascii_lowercase:
		case1 = char in str_set1
		case2 = char in str_set2
		if case1 != case2:
			print(char, end='')
	print()


if __name__ == '__main__':
	t = int(input())
	for i in range(t):
		string1 = input()
		string2 = input()
		uncom_char(string1, string2)	