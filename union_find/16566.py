import bisect

N, M, K = map(int, input().split())

cards = list(map(int, input().split()))

cmd = list(map(int, input().split()))

cards.sort()

parent = list(range(0, len(cards)))

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
        return parent[a]
    return a

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[b] = a
    else:
        parent[a] = b

for c in cmd:
    i = bisect.bisect_right(cards, c)

    i = find(i)

    print(cards[i])

    if i > len(cards)-2:
        continue
    union(i, i + 1)
