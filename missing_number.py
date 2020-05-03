'''
https://practice.geeksforgeeks.org/problems/missing-number-in-array/0
'''

# search numbers from 1 to n
# first missing will be our answer

'''
searching
  liniar n
  binary logn + sorting

  compexity -> nlogn


for i in range(1, 10):
	search(i)
	if not found:
		print()
'''
#######
'''
for i in range(1, 10):
    i == lis[i-1]

 complexity -> n + nlogn
'''
########
'''
n
sum(1-10) - sum(input)
'''

def missing_number(lis, n):
	lis = sorted(lis)
	for i in range(1, n):
		if i != lis[i-1]:
			return i
	return i+1


if __name__ == '__main__':
	t = int(input())
	for i in range(t):
		n = int(input())
		lis = list(map(int, input().split()))
		ans = missing_number(lis, n)
		print(ans)

