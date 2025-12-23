import sys
input = sys.stdin.readline
G = int(input())
P = int(input())

parent = list(range(G+1))

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
        return parent[a]
    return a

# a < b
def union(a, b):
    a = find(a)
    b = find(b)

    parent[b] = a

answer = 0

for _ in range(P):
    p = int(input())

    dock = find(p)

    if dock == 0:
        break
    else:
        union(dock - 1, dock)
        answer += 1
print(answer) 
    