import sys

class Node:
    def __init__(self):
        self.number = False
        self.children = dict()
def search():
    dictionary = Node()

    data = []
    n = int(input())
    for _ in range(n):
        data.append(sys.stdin.readline().rstrip())
    data.sort(key=lambda s:len(s))

    for i in range(n):
        current = dictionary
        s = data[i]

        for i in range(len(s)):
            char = s[i]
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]

            if current.number:
                return "NO"
            
        current.number = True
    return "YES"

answer = []
for _ in range(int(input())):
    answer.append(search())

for a in answer:
    print(a)