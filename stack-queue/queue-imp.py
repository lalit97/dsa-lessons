class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, data):
        """
        add item to queue
        """

    def remove(self):
        """
        remove item from queue
        return: data of removed item
        """

    def peek(self):
        """
        check first item of queue
        return: data of first item
        """

    def is_empty(self):
        """
        check if queue is empty
        return: True or False
        """

    def traverse(self):
        """
        print queue items
        """


if __name__ == '__main__':
    q = Queue()
    q.add(5)
    q.add(10)
    q.add(15)
    q.add(20)
    q.add(30)
    q.remove()
    q.remove()
    q.traverse()
