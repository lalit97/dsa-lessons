"""
Problem not avaliable on GFG
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
			new_node = Node(data)
			curr.next = new_node
		return self.head
	
"""
complete this function
head is given,
task is to print linked list in reverse
"""
def reverse_print(head):
    if head is not None:
        reverse_print(head.next)
        print(head.data, end=" ")

def direct_print(head):
    if head is not None:
        print(head.data, end=" ")
        direct_print(head.next)


"""
rp(1)
rp(2)
rp(3)
rp(4)
rp(5)
rp(5.next)
5 4 3 2 1
"""

if __name__ == '__main__':
    linked_list = LinkedList()
    lis = [1, 2, 3, 4, 5]
    for item in lis:
        linked_list.insert(item)
    #linked_list.traverse()
    head = linked_list.head
    reverse_print(head)
