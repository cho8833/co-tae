from collections import deque

N = int(input())

time = []

indegree = [0] * N

graph = [[] for _ in range(N)]

for n in range(N):
    t = list(map(int, input().split()))
    time.append(t[0])
    i = 1
    while t[i] != -1:
        indegree[n] += 1
        graph[t[i]-1].append(n)
        i += 1

dp = [0] * N

hq = deque()
for i in range(N):
    if indegree[i] == 0:
        hq.append(i)
        dp[i] = time[i]


while hq:
    i = hq.popleft()

    for adj in graph[i]:
        if dp[adj] < dp[i] + time[adj]:
            dp[adj] = dp[i] + time[adj]
            hq.append(adj)
for a in dp:
    print(a)