import sys

def bellmanFord(graph, start, n):
    dist = [0] * (n+1)

    for i in range(n):
        for g in graph:
            if dist[g[0]] != float('inf') and dist[g[1]] > dist[g[0]] + g[2]:
                dist[g[1]] = dist[g[0]] + g[2]
        
                if i == n-1:
                    print("YES")
                    return
        
    print("NO")

for _ in range(int(input())):
    N, M, W = map(int, input().split())
    graph = []
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().rstrip().split())
        graph.append((S, E, T))
        graph.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().rstrip().split())
        graph.append((S, E, -T))

    bellmanFord(graph, 1, N)
    