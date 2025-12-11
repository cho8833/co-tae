import sys
import bisect

N = int(input())

graph = []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph.append((a, b))

graph.sort(key=lambda x:x[0])

lis = []
lis_idx = []
prev_idx = [-1] * N

for i in range(N):
    l = bisect.bisect_left(lis, graph[i][1])
    if l == len(lis):
        lis.append(graph[i][1])
        lis_idx.append(i)
    else:
        lis[l] = graph[i][1]
        lis_idx[l] = i

    if l > 0:
        prev_idx[i] = lis_idx[l-1]

answer = set()

k = lis_idx[-1]

while k != -1:
    answer.add(graph[k][0])
    k = prev_idx[k]

print(N - len(lis))

for g in graph:
    if g[0] not in answer:
        print(g[0])
