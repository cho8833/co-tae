import sys
from collections import deque

T = int(input())

answer = []
for _ in range(T):

    N, K = map(int, input().split())
    D = [0]
    D.extend(list(map(int, input().split())))
    graph = [[] for _ in range(N+1)]
    dp = [0] * (N+1)

    indegree = [0] * (N+1)
        

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().rstrip().split())
        graph[X].append(Y)
        indegree[Y] += 1
    
    # topology sort
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            dp[i] = D[i]
            q.append(i)
    
    W = int(input())

    while q:
        n = q.popleft()
        
        for adj in graph[n]:    
            dp[adj] = max(dp[n] + D[adj], dp[adj])
            indegree[adj] -= 1
            if indegree[adj] == 0:
                q.append(adj)

    answer.append(dp[W])
    
for a in answer:
    print(a)
