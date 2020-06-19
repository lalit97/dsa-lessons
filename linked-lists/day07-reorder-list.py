"""
https://practice.geeksforgeeks.org/problems/reorder-list/1
"""

'''
# Node Class    
class node:
	def __init__(self, val):
		self.data = val
		self.next = None
'''

'''
# Linked List Class
class Linked_List:
	def __init__(self):
		self.head = None
		self.tail = None
'''

"""
task: reorder the list as required
"""
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None
	
	def insert(self, data):
		if self.head is None:
			self.head = Node(data)
		else:
			curr = self.head
			while curr.next is not None:
				curr = curr.next
			curr.next = Node(data)
		return self.head
 
	def reorderList(self):
		if self.head is None or self.head.next is None:
			return None
		middle = get_middle_node(self.head)
		head_b = reverse_list(middle)
		reorder_helper(self.head, head_b)
		curr = self.head
		while curr is not None:
			print(curr.data, end=' ')
			curr = curr.next


def reorder_helper(head_a, head_b):
	p = head_a
	q = head_b
	while q is not None:
		temp = p.next
		p.next = q
		p = temp
		temp = q.next
		q.next = p
		q = temp


def reverse_list(node):
	if node.next is None:
		return node
	new_head = reverse_list(node.next)
	node.next.next = node
	node.next = None
	return new_head


def get_middle_node(head):
	slow, fast = head, head 
	while fast is not None and fast.next is not None:
		slow = slow.next
		fast = fast.next.next
	middle = slow.next
	slow.next = None
	return middle
	

if __name__ == '__main__':
	llist = LinkedList()
	items = [1, 2, 3, 4, 5]
	for item in items:
		llist.insert(item)
	llist.reorderList()
	# curr = llist.head
	# while curr is not None:
	#     print(curr.data, end=' ')
	#     curr = curr.next


def reorder_helper(head_a, head_b):
	p = head_a
	q = head_b
	while q is not None:
		temp = p.next
		p.next = q
		p = temp
		temp = q.next
		q.next = p
		q = temp


def reverse_list(head):
    curr = head
    prev = None
    next = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def get_middle_node(head):
	slow, fast = head, head 
	while fast is not None and fast.next is not None:
		slow = slow.next
		fast = fast.next.next
	middle = slow.next
	slow.next = None
	return middle


def reorderList(self):
	if (self.head==None or self.head.next==None):
		return
	middle = get_middle_node(self.head)
	head_b = reverse_list(middle)
	reorder_helper(self.head, head_b)