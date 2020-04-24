class ListNode:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)  # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0  # nie trzeba obliczać za kaŜdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def count(self):  # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, list_node):
        if self.length == 0:
            self.head = self.tail = list_node
        else:  # dajemy na koniec listy
            list_node.next = self.head
            self.head = list_node
        self.length += 1

    def insert_tail(self, list_node):  # klasy O(N)
        if self.length == 0:
            self.head = self.tail = list_node
        else:  # dajemy na koniec listy
            self.tail.next = list_node
            self.tail = list_node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.length == 0:
            raise ValueError("pusta lista")
        list_node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        list_node.next = None  # czyszczenie łącza
        self.length -= 1
        return list_node  # zwracamy usuwany node

    def print_list(self):
        for i in range(self.count()):
            print(self.remove_head())


class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None, up=None):
        self.data = data
        self.left = left
        self.right = right
        self.up = up

    def __str__(self):
        return str(self.data)

    def __int__(self):
        try:
            return int(self.data)
        except ValueError:
            print("Zły typ danych")
            return 0

    def horizontal_searching(self):
        queue = SingleList()
        temporary_queue = SingleList()
        temporary_queue.insert_tail(self)
        while temporary_queue.is_empty() is False:
            v = temporary_queue.remove_head()
            if v.left is not None:
                temporary_queue.insert_tail(v.left)
            if v.right is not None:
                temporary_queue.insert_tail(v.right)
            queue.insert_tail(v)
        return queue

    def vertical_searching(self):
        queue = SingleList()
        temporary_queue = SingleList()
        temporary_queue.insert_head(self)
        while temporary_queue.is_empty() is False:
            v = temporary_queue.remove_head()
            if v.right is not None:
                temporary_queue.insert_head(v.right)
            if v.left is not None:
                temporary_queue.insert_head(v.left)
            queue.insert_tail(v)
        return queue

    def new_node(self, new_root):

        if new_root.left is not None or new_root.right is not None:
            raise Exception ("Podany wierzchołek nie jest liściem")
            return None

        temporary_queue = SingleList()
        temporary_queue.insert_tail(self)
        while temporary_queue.is_empty() is False:
            el = temporary_queue.remove_head()
            if el.left is not None:
                temporary_queue.insert_tail(el.left)
                el.left.up = el
            if el.right is not None:
                temporary_queue.insert_tail(el.right)
                el.right.up = el

        node = new_root
        # ta linijka tylko dla roota
        dad = node.up
        node.right = dad
        previous = node
        node = dad

        # pętla do dojścia do starego roota
        while node.up:
            dad = node.up
            if previous == node.right:
                node.right = dad
            if previous == node.left:
                node.left = dad
            previous = node
            node = dad
        if node.left == previous:
            node.left = None
        else:
            node.right = None



        return new_root


def traverse_preorder(top):
    if top is None:
       return
    print(top)
    print
    traverse_preorder(top.left)
    traverse_preorder(top.right)


# tworzymy drzewo binarne
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)

traverse_preorder(root)
print('finished')

new_root= root.new_node(root.right.right.left)
traverse_preorder(new_root)
