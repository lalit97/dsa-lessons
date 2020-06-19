"""
https://practice.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1
"""

'''
Function to merge two sorted lists in one
using constant space.

Function Arguments: head_a and head_b (head reference of both the sorted lists)
Return Type: head of the obtained list after merger.
'''

def merge(head_a,head_b):
    dummy = Node(0)
    curr = dummy
    while head_a is not None or head_b is not None:
        if head_a.data > head_b.data:
            curr.next = head_a
            head_a = head_a.next
        else:
            curr.next = head_b
            head_b = head_b.next
        curr = curr.next

    while head_a is not None:
        curr.next = head_a
        curr = curr.next
        head_a = head_a.next

    while head_b is not None:
        curr.next = head_b
        curr = curr.next
        head_b = head_b.next
    
    return dummy.next