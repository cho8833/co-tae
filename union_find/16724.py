import sys
N, M = map(int ,input().split())

parent = list(range(N * M))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(N):
    row = list(sys.stdin.readline())

    for j in range(M):
        n = i * M + j
        if row[j] == 'L':
            union(n, n-1)
        elif row[j] == "R":
            union(n, n+1)
        elif row[j] == "U":
            union(n, n-M)
        elif row[j] == "D":
            union(n, n+M)

for r in range(N):
    for c in range(M):
        n = r * M + c
        find(n)

print(len(set(parent)))