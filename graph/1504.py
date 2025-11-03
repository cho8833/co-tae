import sys
from collections import deque
N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start, target):
    dist = [float('inf')] * (N+1)

    queue = deque()
    dist[start] = 0
    queue.append((start, 0))

    while queue:
        n, d = queue.popleft()

        if dist[n] < d:
            continue
        
        for node in graph[n]:
            path = node[1] + d
            if path < dist[node[0]]:
                dist[node[0]] = path
                queue.append((node[0], path))
    return dist[target]

s2v1 = dijkstra(1, v1)
s2v2 = dijkstra(1, v2)
v12v2 = dijkstra(v1,v2)
v12end = dijkstra(v1, N)
v22end = dijkstra(v2, N)

answer1 = s2v1+v12v2+v22end
answer2 = s2v2+v12v2+v12end

if answer1 == float('inf'):
    if answer2 == float('inf'):
        print(-1)
    else:
        print(answer2)
else:
    if answer2 == float('inf'):
        print(answer1)
    else:
        print(min(answer1, answer2))