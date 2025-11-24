import sys
sys.setrecursionlimit(10**6)
N, R, Q = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, sys.stdin.readline().rstrip().split())
    graph[U].append(V)
    graph[V].append(U)

size = [0] * (N+1)

child = [[] for _ in range(N+1)]

def makeTree(c, p):
    for node in graph[c]:
        if node != p:
            child[c].append(node)
            makeTree(node, c)

def countSubtreeNodes(c):
    size[c] = 1
    for node in child[c]:
        countSubtreeNodes(node)
        size[c] += size[node]

makeTree(R, -1)
countSubtreeNodes(R)

answer = []
for _ in range(Q):
    print(size[int(sys.stdin.readline())])
