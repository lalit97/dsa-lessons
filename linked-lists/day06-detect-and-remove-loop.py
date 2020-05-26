"""
https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1
"""

"""
Detect if there is a loop present in the linked list
if present try to remove that.
""" 


def removeTheLoop(head):
    if head is None or head.next is None:
        return None
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # in case there was a loop
    if slow == fast:
        slow = head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None

"""
Reason 1
slow == fast
let,
slow -> i
fast -> i + 1

one step behind
slow -> i - 1
fast -> i - 1
"""

"""
Reason 2
without loop linkedlist size = k 
loop_size = t

slow = head, fast = head

slow -> k steps 
fast -> 2k steps

fast inside loop -> 2k - k = k steps

distance between fast & slow = t - k
fast will take t-k steps to catch slow
so basically when slow takes t - k steps fast will catch it

# after catching 

loop size = t 
slow walks = t - k 
left loop size = t - (t-k) = k 

so we move slow to the head 
and increase fast & slow by 1 step at a time

"""