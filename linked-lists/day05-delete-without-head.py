"""
https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1
"""

"""
Your task is to delete the given node from
the linked list, without using head pointer.

Function Arguments: node (given node to be deleted) 
Return Type: None, just delete the given node from the linked list.
"""

1 -> 2 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 


def deleteNode(curr):
    if curr is None:
        return None
    while curr.next.next is not None:
        curr.data = curr.next.data
        curr = curr.next
    curr.data = curr.next.data
    curr.next = None

"""
alternate solution
def deleteNode(curr):
    if curr is None:
        return None
    next_node = curr.next
    curr.data = next_node.data
    to_delete = next_node
    curr.next = next_node.next
    to_delete.next = None
"""
