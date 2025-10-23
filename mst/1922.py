import sys
N = int(input())
M = int(input())

graph = []

for _ in range(M):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

graph.sort(key = lambda x:x[2])

parent = list(range(N+1))

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a

answer = 0
for a, b, c in graph:
    if (find(a) != find(b)):
        union(a,b)
        answer += c
print(answer)