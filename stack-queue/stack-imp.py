class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        """ push the new node in stack
        argument: data of new node
        return: none
        """

    def pop(self):
        """
        remove the top most item from stack
        return: the removed node
        """


    def peek(self):
        """
        return: the data of top element
        """


    def traverse(self):
        """
        print items of stack
        return: none
        """

    def is_empty(self):
        """
        check of stack is empty or not
        return: True or False
        """


if __name__ == '__main__':
    MyStack = Stack()
    MyStack.push(5)
    MyStack.push(10)
    MyStack.push(15)
    MyStack.push(25)
    MyStack.push(35)
    MyStack.pop()
    MyStack.pop()
    MyStack.pop()
    MyStack.traverse()