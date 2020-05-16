

#init -> initializer
"""

class Integer:
	def __init__(self, data):
		self.data = data

class Table:
	def __init__(self, w, h, color):
		self.w = w 
		self.h = h
		self.color = color 
	


t1 = Table(4,5,'white')


Integer -> 4
Char = 'C'
Table -> width, height, colour
(data, next)


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
	
	def traverse(self):
		if self.head is None:
			return None
		curr = self.head 
		while curr is not None:
			print(curr.data, end='->')
			curr = curr.next
	
	def insert_after(self, item, new):
		if self.head is None:
			return None
		curr = self.head
		while curr.data != item:
			curr = curr.next

		temp = curr.next
		new_node = Node(new)
		curr.next = new_node
		new_node.next = temp
		

if __name__ == '__main__':
	linked_list = LinkedList()
	#print(linked_list.head)
	linked_list.insert(5)
	#print(linked_list.head.data)
	linked_list.insert(8)
	#print(linked_list.head.next.data)
	linked_list.insert(14)
	#print(linked_list.head.next.next.data)
	#linked_list.traverse()
	linked_list.insert_after(8, 15)
	linked_list.traverse()