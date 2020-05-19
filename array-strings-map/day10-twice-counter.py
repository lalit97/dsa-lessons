"""
https://practice.geeksforgeeks.org/problems/twice-counter/0
# ["hate", "this", "this", "hate", "that"] 
# {"hate":2, "this":2, "that":1}
# answer -> 2
"""

def get_counter(words):
	counter = {}
	for word in words:
		if word not in counter:
			counter[word] = 1
		else:
			counter[word] += 1
	return counter


def twice_counter(string, length):
	count = 0
	words = string.split()
	counter = get_counter(words)
	for word in counter:
		if counter[word] == 2:
			count += 1
	return count


if __name__ == '__main__':
	for _ in range(int(input())):
		length = int(input())
		string = input()
		ans = twice_counter(string, length)
		print(ans)