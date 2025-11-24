import sys

n, m = map(int, input().split())

parent = list(range(n))

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

for i in range(1, m+1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if find(a) != find(b):
        union(a, b)
    else:
        print(i)
        exit()
print(0)