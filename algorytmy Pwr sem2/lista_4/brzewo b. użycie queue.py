
class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class NodeQ:

    def __init__(self, data):
        self.data = data
        self.next = None

# A class to represent a queue

# The queue, front stores the front node of LL and rear stores the last node of LL

class Queue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    # Method to add an item to the queue
    def enQueue(self, item):
        temp = NodeQ(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    # method to remove an item from queue

    def deQueue(self):

        if self.isEmpty():
            return

        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None

        return temp.data



def traverse_preorder(top):
    if top is None:
       return
    print(top)
    traverse_preorder(top.left)
    traverse_preorder(top.right)

def traverse_queue(top):
    if top is None:
        return
    queue = Queue()
    queue.enQueue(top)
    while not queue.isEmpty():
        node = queue.deQueue()
        print(node)
        if node.left:
            queue.enQueue(node.left)
        if node.right:
            queue.enQueue(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# traverse_preorder(root) #sprawdzam, czy drzewo działa

traverse_queue(root)