from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    visit = [0] * n
    queue = deque([i])
    while queue:
        j = queue.pop()
        
        for ad in range(n):
            if visit[ad] == 0 and graph[j][ad] == 1:
                visit[ad] = 1
                queue.append(ad)
    print(" ".join(list(map(str, visit))))