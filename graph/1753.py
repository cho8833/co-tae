import sys
import heapq

v, e = map(int, input().split())

k = int(input())

# data[1] = [[n, w]] : 2번 노드에 연결된 노드들과 가중치

data = [[] for _ in range(v)]

for _ in range(e):
    f, t, w = map(int, sys.stdin.readline().split())

    data[f-1].append([t-1, w])

# init table
table = [float('inf') for _ in range(v)]

table[k-1] = 0

hq = []
heapq.heappush(hq, (0, k-1))

while len(hq) != 0:
    dist, now = heapq.heappop(hq)

    if table[now] < dist:
        continue
    
    for node in data[now]:
        if dist+node[1] < table[node[0]]:
            table[node[0]] = dist+node[1]
            heapq.heappush(hq, (dist+node[1], node[0]))

for dist in table:
    if dist == float('inf'):
        print('INF')
    else:
        print(dist)
