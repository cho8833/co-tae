import sys
import heapq

N = int(input())

M = int(input())


graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b,c))


def dijkstra(start, end):
    dist = [float('inf')] * (N+1)

    visited = list(range(N+1))

    dist[start] = 0

    queue = []

    queue.append((start, 0))

    while queue:
        n, c = heapq.heappop(queue)

        if c > dist[n]:
            continue

        for adj in graph[n]:
            m, d = adj


            if dist[m] > dist[n] + d:
                dist[m] = dist[n] + d
                visited[m] = n
                heapq.heappush(queue, (m, dist[m]))

    print(dist[end])
    
    cities = []
    def find(n):
        cities.append(n)
        if n != start:    
            find(visited[n])
            
    find(end)
    print(len(cities))
    for i in range(len(cities)-1, -1, -1):
        print(cities[i], end=' ')
    

start, end = map(int, input().split())

dijkstra(start, end)