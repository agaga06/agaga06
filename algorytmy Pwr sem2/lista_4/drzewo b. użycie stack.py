class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class NodeS:
    """Klasa reprezentująca węzeł do stosu."""
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = NodeS(data)
        else:
            new_node = NodeS(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def isEmpty(self):
        return self.head == None



def traverse_preorder(top):
    #funkcja przechodzenia przez drzewo rekurencyjnie
    if top is None:
        return
    print(top)
    traverse_preorder(top.left)
    traverse_preorder(top.right)


def traverse_stack(top):
    if top is None:
        return
    stack = Stack()
    stack.push(top)
    while not stack.isEmpty():
        node = stack.pop()
        print(node)
        if node.right:
            stack.push(node.right)
        if node.left:
            stack.push(node.left)


#tworzę drzewo

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

#traverse_preorder(root) #sprawdzam, czy drzewo działa

traverse_stack(root)