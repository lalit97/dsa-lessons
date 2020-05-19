"""
https://practice.geeksforgeeks.org/problems/check-if-a-string-is-isogram-or-not-1587115620/1
"""




def isIsogram(string):
	lookup = set()
	for char in string:
		if char not in lookup:
			lookup.add(char)
		else:
			return False
	return True

