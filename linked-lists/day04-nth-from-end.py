"""
https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1
"""

"""
Your task is to return the data stored in
the nth end from end of linked list.
"""
"""
can be done by either of the 3 methods

-> Brute Force simple traversal (length nikal sakte hain) (done)

-> 2 pointers(not runner up technique) + simple maths 

-> recursion
"""

def getNthfromEnd(head, n):
    p1 = head
    p2 = head
    for i in range(n):
        if p1 is None:
            return -1
        p1 = p1.next

    while p1 is not None:
        p1 = p1.next
        p2 = p2.next
    return p2.data


"""
    lenght = 9
    end = 2nd
    front = 8th
"""