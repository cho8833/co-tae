import sys

N, M = map(int, input().split())

graph = []

cost = []

for i in range(M):
    A, B, C = map(int, sys.stdin.readline().rstrip().split())
    cost.append((C, i))
    graph.append((A,B))

cost.sort(reverse=True)

parent = list(range(N+1))

v = set(range(N+1))

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
        return parent[a]
    return a

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
        v.remove(b)
    else:
        parent[a] = b
        v.remove(a)

answer = 0

while cost:
    if len(v)-1 == 2:
        break
    c, i = cost.pop()
    
    a, b = graph[i]

    if find(a) != find(b):
        union(a, b)
        answer += c
print(answer)
