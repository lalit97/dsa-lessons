"""
https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1
"""

"""
Method -> 1 (Traversal)
def get_length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def findMid(head):
    length = get_length(head)
    middle = length // 2
    for i in range(middle):
        head = head.next
    return head
"""

#Method ->2 (Runner up)

def findMid(head):
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    if fast.next is None:
        return slow
    return slow.next

