from collections import deque

N, M, X = map(int, input().split())

time = [0] * N

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e,t))

def dijkstra(start, target):
    dist = [1e7] * (N+1)

    dist[start] = 0
    queue = deque()
    queue.append((start, 0))

    while queue:
        n, d = queue.popleft()

        if dist[n] < d:
            continue
        
        for node in graph[n]:
            if d + node[1] < dist[node[0]]:
                dist[node[0]] = d + node[1]
                queue.append((node[0], node[1] + d))
    return dist[target]

answer = [0] * (N+1)
# 각 노드에 대해 가는 길 다익스트라
for i in range(1, len(graph)):
    if i == X:
        continue
    answer[i] = dijkstra(i, X)

# 각 노드에 대해 오늘 길 다익스트라
for i in range(1, len(graph)):
    if i == X:
        continue
    answer[i] += dijkstra(X, i)

print(max(answer))