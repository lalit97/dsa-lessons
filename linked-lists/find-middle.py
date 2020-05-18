
"""
traverse and solve

recursion -> 

runner technique -> 
    fast pointer slow pointer 
    fast = fast.next.next
    slow = slow.next


1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
"""

# length = len(array)

# array = [1,2,3,4,5]
# length = 0
# for item in arr:
#     length += 1
# return length

length = 0
curr = self.head
while curr is not None:
    curr = curr.next
    length += 1

##
curr = head
for i in range(length//2):
    curr.next
return head.data

########################

slow = self.head
fast = self.head
while fast is not None:
    slow = slow.next
    fast = fast.next.next
return slow.data