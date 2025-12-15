import sys
input = sys.stdin.readline

for _ in range(int(input())):
    F = int(input())

    parent = []
    count = dict()
    id = 0
    idMap = dict()

    def find(a):
        if parent[a] != a:
            parent[a] = find(parent[a])
            return parent[a]
        return a
    
    def union(a, b):
        a = find(a)
        b = find(b)

        if a == b:
            return

        if a < b:
            parent[b] = a
            count[a] += count[b]
        else:
            parent[a] = b
            count[b] += count[a]

    for _ in range(F):
        id1, id2 = input().rstrip().split()

        if id1 not in idMap:
            idMap[id1] = id
            parent.append(id)
            count[id] = 1
            id += 1
        if id2 not in idMap:
            idMap[id2] = id
            parent.append(id)
            count[id] = 1
            id += 1

        union(idMap[id1], idMap[id2])

        relation = find(idMap[id1])

        print(count[relation])