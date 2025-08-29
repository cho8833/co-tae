class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = Node(root)
    def insert(self, value):
        self.root = self._insert_value(self.root, value)
        return self.root is not None
    def _insert_value(self, node, value):
        if node is None:
            node = Node(value)
            return
        if node.value > value:
            self._insert_value(node.right, value)
        else:
            self._insert_value(node.left, value)

data = {}
for _ in range(int(input())):
    n1, n2 = input().split(' ')
    if n2 in data:
        data[n2].insert(int(n1))
    else:
        data[n2] = BST(int(n1))
    
for y in data.keys():
    print(y)
