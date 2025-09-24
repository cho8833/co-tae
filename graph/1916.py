import sys
import heapq

n = int(input())
m = int(input())
data = [[] for _ in range(n)]

for _ in range(m):
    v, e, w = map(int, sys.stdin.readline().split())

    data[v-1].append([e-1,w])

start, end = map(int, input().split())

table = [float('inf') for _ in range(n)]

table[start-1] = 0

hq = []
heapq.heappush(hq, (start-1, 0))

while len(hq) != 0:
    n, w = heapq.heappop(hq)
    if table[n] < w or n == end-1:
        continue
    
    for node in data[n]:
        dist = node[1] + w
        if dist < table[node[0]]:
            table[node[0]] = dist
            heapq.heappush(hq, (node[0], dist))
print(table[end-1])