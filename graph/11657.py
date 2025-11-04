import sys

N, M = map(int, input().split())

edges = []

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().rstrip().split())
    edges.append((A, B, C))

dist = [float('inf')] * (N+1)

dist[1] = 0

for i in range(N):
    for e in range(M):
        start = edges[e][0]
        end = edges[e][1]
        weight = edges[e][2]

        if dist[start] != float('inf') and dist[end] > dist[start] + weight:
            dist[end] = dist[start] + weight

            if i == N-1:
                print(-1)
                exit()

for i in range(2, len(dist)):
    if dist[i] == float('inf'):
        print(-1)
    else:
        print(dist[i])
