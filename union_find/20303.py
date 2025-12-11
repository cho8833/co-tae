import sys

N, M, K = map(int, input().split())
candies = [0]
candies.extend(list(map(int, input().split())))

parent = list(range(N+1))

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
        return parent[a]
    return a

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    union(a, b)

group = dict()

for i in range(1, N+1):
    p = find(i)
    if p not in group:
        group[p] = [1, candies[i]]
    else:
        group[p][0] += 1
        group[p][1] += candies[i]

dp = [0] * (K)
for d in group.values():
    kid = d[0]
    if kid >= K:
        continue
    candy = d[1]
    for i in range(K-1-kid, -1, -1):
        if dp[i] != 0:
            dp[i+kid] = max(dp[i+kid], dp[i] + candy)
    dp[kid] = max(dp[kid], candy)
print(max(dp))


