"""
https://practice.geeksforgeeks.org/problems/parenthesis-checker/0
"""
"""
task is to complete function 
is_balanced() 
return: 'balanced' or 'not balanced'


hint: use Stack DS
fill push and pop methods
and you can call them
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):

    def pop(self):




def is_balanced(string):
    my_stack = Stack()
                

if __name__ == '__main__':
    for _ in range(int(input())):
        string = input()
        ans = is_balanced(string)
        print(ans)
