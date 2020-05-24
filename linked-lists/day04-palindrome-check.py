"""
https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1
"""
"""
Your task is to check if given linkedlist is a pallindrome or not.
complete the function isPalindrome()
return True or False
"""
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None


# class LinkedList:
# 	def __init__(self):
# 		self.head = None
	
# 	def insert(self, data):
# 		if self.head is None:
# 			self.head = Node(data)
# 		else:
# 			curr = self.head
# 			while curr.next is not None:
# 				curr = curr.next
# 			new_node = Node(data)
# 			curr.next = new_node
# 		return self.head


def reverse_list(node):
	rev_head = None
	while node is not None:
		n = Node(node.data)
		n.next = rev_head
		rev_head = n
		node = node.next
	return rev_head


def is_equal(head,reverse_head):
	while head is not None:
		if reverse_head.data != head.data:
			return False
		head = head.next
		reverse_head = reverse_head.next
	return True


def isPalindrome(head):
	reverse_head = reverse_list(head)
	answer = is_equal(head,reverse_head)
	return answer  


# if __name__ == '__main__':
# 	linked_list = LinkedList()
# 	items = [1,2,4,1]
# 	for item in items:
# 		linked_list.insert(item)
# 	head = linked_list.head
# 	ans = isPalindrome(head)
# 	print(ans)


