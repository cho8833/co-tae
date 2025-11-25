N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

indegree = [0] * (N+1)

for _ in range(M):
    order = list(map(int, input().split()))[1:]

    for i in range(len(order)-1):
        graph[order[i]].append(order[i+1])
        indegree[order[i+1]] += 1

q = []

for i in range(1, len(indegree)):
    if indegree[i] == 0:
        q.append(i)

answer = []
while q:
    n = q.pop()

    answer.append(n)

    for adj in graph[n]:
        indegree[adj] -= 1

        if indegree[adj] == 0:
            q.append(adj)

if max(indegree) > 0:
    print(0)
else:
    for a in answer:
        print(a)
            
    