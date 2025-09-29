import sys
import heapq
sys.setrecursionlimit(100001)
n = int(input())
data = dict()

for _ in range(n):
    s = list(map(int, sys.stdin.readline().strip().split()))
    p = s[0]
    i = 1
    data[p] = []

    while True:
        if s[i] == -1:
            break
        
        data[p].append((s[i], s[i+1]))
        i+= 2

visited = [False for _ in range(n+1)]
result = 0
def dfs(node):
    global visited
    global result
    visited[node] = True

    adjusts = data[node]
    w = 0
    weights = []
    for ad in adjusts:
        if not visited[ad[0]]:
            path = dfs(ad[0]) + ad[1]
            heapq.heappush(weights, -path)
            w = max(w, path)
            
    if len(weights) > 1:
        result = max(result, -heapq.heappop(weights) - heapq.heappop(weights))
    elif len(weights) == 1:
        result = max(result, -weights[0])
    return w

dfs(1)
print(result)