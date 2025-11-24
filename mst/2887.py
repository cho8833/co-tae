import sys

N = int(input())

xs = []
ys = []
zs = []

for i in range(N):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())

    xs.append((x, i))
    ys.append((y, i))
    zs.append((z, i))

xs.sort(key=lambda x:x[0])
ys.sort(key=lambda x:x[0])
zs.sort(key=lambda x:x[0])

parent = list(range(N))

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
        return parent[a]
    return a

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

costs = []

for i in range(N-1):
    costs.append((abs(xs[i][0] - xs[i+1][0]), xs[i][1], xs[i+1][1]))
    costs.append((abs(ys[i][0] - ys[i+1][0]), ys[i][1], ys[i+1][1]))
    costs.append((abs(zs[i][0] - zs[i+1][0]), zs[i][1], zs[i+1][1]))

costs.sort(key=lambda x: x[0])

answer = 0

for c, a, b in costs:
    if find(a) != find(b):
        answer += c
        union(a,b)
print(answer)