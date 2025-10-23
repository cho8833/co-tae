n = int(input())

stars = []

for _ in range(n):
    stars.append(list(map(float, input().split())))

graph = []
parent = {}

for i in range(len(stars)):
    parent[i] = i
    for j in range(i+1, len(stars)):
        graph.append([i, j, (stars[j][0] - stars[i][0]) ** 2 + (stars[j][1] - stars[i][1]) ** 2])

graph.sort(key = lambda x: x[2])

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a
answer = 0
for a, b, c in graph:
    if find(a) != find(b):
        union(a, b)
        answer += c ** (1/2)
print("{0:.2f}".format(answer))
