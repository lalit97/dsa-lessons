"""
https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1
"""

"""
1 -> 2 -> 3 ->

<- 1 <- 2 <- 3

[1,2,3,4]
for item arr[::-1]:
    print(item) 4, 3, 2, 1
print(arr) -> [1,2,3,4]

[4, 3, 2, 1]
for item in arr:
    print(item)
"""

def reverseList(self):
    curr = self.head
    prev = None
    next = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    self.head = prev
    return self.head


"""
Recursive
def reverseList(self):
    node = self.head
    ans = helper(node)
    self.head = ans
    return self.head


def helper(node):
    if node is None or node.next is None:
        return node
    else:
        new_head = helper(node.next)
        node.next.next = node
        node.next = None
        return new_head
"""
