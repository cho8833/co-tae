import sys
import heapq
N, M = map(int, input().split())

indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    graph[A].append(B)
    indegree[B] += 1

popable = []
for i in range(1, len(indegree)):
    if indegree[i] == 0:
        heapq.heappush(popable, i)

answer = []
while popable:
    n = heapq.heappop(popable)

    answer.append(n)

    for adj in graph[n]:
        indegree[adj] -= 1
        if indegree[adj] < 1:
            heapq.heappush(popable, adj)

print(" ".join(map(str, answer)))