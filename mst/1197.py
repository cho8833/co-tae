import sys

V, E = map(int, input().split())

graph = []

for i in range(E):
    # [0] 번 정점, [1] 번 정점이 가중치 [2] 로 연결
    node = list(map(int, sys.stdin.readline().rstrip().split()))
    node[0] -= 1
    node[1] -= 1
    graph.append(node)

graph.sort(key=lambda x:x[2])
parent = list(range(V))

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a
answer = 0
for a,b,c in graph:
    if find(a) != find(b):
        union(a,b)
        answer += c
print(answer)

