n, m, r = map(int, input().split())

items = [0]
items.extend(list(map(int, input().split())))

graph = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

def dfs(node, dist, visited):
    total = 0
    
    if not visited[node]:
        total += items[node]
        visited[node] = True

    for adj in graph[node]:
        if adj[1] + dist <= m:
            total += dfs(adj[0], dist + adj[1], visited)

    return total

answer = 0
for start in range(1, len(items)):
    visited = [False] * (n+1)
    total = dfs(start, 0, visited)
    answer = max(total, answer)

print(answer)
