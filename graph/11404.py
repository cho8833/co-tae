import sys

n = int(input())
m = int(input())



graph = [[float('inf')] * n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0    

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(n):
    for b in range(n):
        if graph[a][b] == float('inf'):
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
        