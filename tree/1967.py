import sys
import heapq
sys.setrecursionlimit(20001)
n = int(input())

data = dict()

result = 0

for _ in range(n-1):
    p, c, w = map(int, sys.stdin.readline().strip().split())

    if p not in data:
        data[p] = [(c, w)]
    else:
        data[p].append((c,w))

    if c not in data:
        data[c] = [(p, w)]
    else:
        data[c].append((p, w))

visited = [False for _ in range(n+1)]

if n == 1:
    print(0)
    exit()

def dfs(node):
    global result
    global visited
    w = 0
    adjusts = data[node]
    visited[node] = True

    weights = []

    for ad in adjusts:
        if not visited[ad[0]]:
            path = ad[1] + dfs(ad[0])
            w = max(w, path)
            heapq.heappush(weights, -path)
    if len(weights) > 1:
        result = max(result, -heapq.heappop(weights) -heapq.heappop(weights))
    elif len(weights) == 1:
        result = max(result, -weights[0])
    return w

dfs(1)
print(result)