import sys
sys.setrecursionlimit(10**6)

for _ in range(int(input())):
    N = int(input())
    graph = [0]
    graph.extend(list(map(int, input().split())))

    visited = [False] * (N+1)

    teams = 0

    def dfs(team, node):
        global teams
        if visited[node]:
            if node in team:
                for i in range(len(team)-1, -1, -1):
                    teams += 1
                    if team[i] == node:
                        break
            return
        else:
            visited[node] = True
            team.append(node)
            dfs(team, graph[node])
            
        
    for i in range(1, N+1):
        if not visited[i]: 
            visited[i] = True
            dfs([i], graph[i])
                
    print(N-teams)