class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder(node):
    result = ""
    if node:
        result += inorder(node.left)
        result += node.value
        result += inorder(node.right)
    return result

def preorder(node):
    result = ""
    if node:
        result += node.value
        result += preorder(node.left)
        result += preorder(node.right)
    return result
def postorder(node):
    result = ""
    if node:
        result += postorder(node.left)
        result += postorder(node.right)
        result += node.value
    return result
n = int(input())

s = list(input().split())

data = dict()
root = Node(s[0])

data[s[0]] = root
if s[1] != ".":
    root.left = Node(s[1])
    data[s[1]] = root.left
if s[2] != ".":
    root.right = Node(s[2])
    data[s[2]] = root.right

for _ in range(n-1):
    node, left, right = input().split()
    if left != '.':
        data[node].left = Node(left)
        data[left] = data[node].left
    if right != ".":
        data[node].right = Node(right)
        data[right] = data[node].right


print(preorder(root))
print(inorder(root))
print(postorder(root))