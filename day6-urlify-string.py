"""
https://practice.geeksforgeeks.org/problems/urlify-a-given-string/0
"""

# def urlify(string, k):
# 	return string.replace(" ", "%20")

def urlify(string, k):
	string = "he ll o"
	length = len(string) 
	temp = list(string)  # ['h', 'e', ' ', 'l', 'l',' ','o']
	answer = ""
	for index in range(length):
		if temp[index] == " ":
			temp[index] = "%20"
		answer += temp[index]   #'he%20ll%20'
	return answer




if __name__ == '__main__':
	for _ in range(int(input())):
		string = input()
		k = input()
		ans = urlify(string, k)
