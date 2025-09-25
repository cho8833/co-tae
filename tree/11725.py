import sys
from collections import deque


n = int(input())

data = dict()
data[1] = []

for _ in range(n-1):
    n1, n2 = map(int, sys.stdin.readline().strip().split())

    if n1 not in data:
        data[n1] = [n2]
    else:
        data[n1].append(n2)
    
    if n2 not in data:
        data[n2] = [n1]
    else:
        data[n2].append(n1)

queue = deque()
visited = [False for _ in range(n)]

result = [0 for _ in range(n)]
queue.append(1)

while queue:
    node = queue.popleft()
    
    visited[node-1] = True

    children = data[node]
    
    for c in children:
        if not visited[c-1]:
            result[c-1] = node
            queue.append(c)

for i in range(1, len(result)):
    print(result[i])