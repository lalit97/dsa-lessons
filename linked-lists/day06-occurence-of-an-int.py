"""
https://practice.geeksforgeeks.org/problems/occurence-of-an-integer-in-a-linked-list/1
"""

""" 
Arguments: linked list head, k
Return: total number of times k present in the linked list.

example

1 -> 2 -> 2 -> 3 -> 2 -> 5
k = 2
return 3 (2 appeares 3 times in list)
"""
def count(head, search_for):
    count = 0
    while head is not None:
        if head.data == search_for:
            count += 1
        head = head.next
    return count