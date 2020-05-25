"""
https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1
"""

"""
Your task is to return the point of intersection
in two linked list, connected in y shaped form.
	
Function Arguments: head_a, head_b (heads of both the lists)
	
Return Type: NODE present at the point of intersection, or -1 if no common point.
"""

1 -> 2 -> 3 -> 8 -> 9 -> 10 -> 12

4 -> 5 -> / 
"""
list1 -> before intersection point length = x
list2 -> before intersection point length = y
after intersection point length = z

x + z + y
y + z + x

3 + 4 + 2
2 + 4 + 3

####
not intersecting
1 -> 2 -> 3 -> 4

5 -> 6 -> 7

4 + 3 = 7
3 + 4 = 7
"""

def intersetPoint(head_a, head_b):
    curr_a = head_a
    curr_b = head_b
    while curr_a != curr_b:
        if curr_a is not None:
            curr_a = curr_a.next
        else:
            curr_a = head_b
        if curr_b is not None:
            curr_b = curr_b.next
        else:
            curr_b = head_a
    if curr_a is None:
        return -1
    return curr_a