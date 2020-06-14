"""
https://practice.geeksforgeeks.org/problems/get-minimum-element-from-stack/1
"""


# User function Template for python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            temp = Node(data)
            temp.next = self.top
            self.top = temp

    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        if self.top is None:
            return True
        return False


class stack:
    def __init__(self):
        self.stack1 = MyStack()
        self.min_vals = MyStack()

    def push(self, x):
        """
        push item to stack
        """

    def pop(self):
        """
        pop and return the element
        if stack is empty return -1
        """

    def getMin(self):
        """
        return the minimum element
        if stack is empty return -1
        """
