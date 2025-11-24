import sys
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

indegree = [0] * (N+1)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    graph[A].append(B)
    indegree[B] += 1
q = []

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    n = q.pop()

    for next in graph[n]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)
    
    print(n, end=" ")
