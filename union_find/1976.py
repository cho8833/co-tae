N = int(input())
M = int(input())

parent = list(range(N+1))

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
        return parent[a]
    return a

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a

for i in range(N):
    conn = list(map(int, input().split()))
    for j in range(N):
        if conn[j] == 1:
            union(i+1, j+1)
plan = list(map(int, input().split()))

temp = find(plan[0])
for city in plan:
    if temp != find(city):
        print("NO")
        exit()
print("YES")