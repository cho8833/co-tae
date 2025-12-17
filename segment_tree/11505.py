import sys
input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())

data = []

for _ in range(N):
    data.append(int(input()))

tree = [0] * (4 * N)

def init(start, end, i):
    if start == end:
        tree[i] = data[start]
    else:
        mid = (start + end) // 2
        tree[i] = init(start, mid, i * 2) * init(mid+1, end, i * 2 + 1) % 1_000_000_007
    return tree[i]

def mult(start, end, i, left, right):
    if left > end or right < start:
        return 1
    if left <= start and right >= end:
        return tree[i]
    mid = (start + end) // 2

    return mult(start, mid, i * 2, left, right) * mult(mid + 1, end, i * 2 + 1, left, right) % 1_000_000_007

def update(start, end, i, target, new):
    if target < start or target > end:
        return tree[i]
    if start == end:
        tree[i] = new
    else:
        mid = (start + end) // 2
        tree[i] = update(start, mid, i * 2, target, new) * update(mid + 1, end, i * 2 + 1, target, new) % 1_000_000_007
    return tree[i]

init(0, N-1, 1)

for _ in range(M+K):
    a, b, c = map(int, input().rstrip().split())

    if a == 1:
        update(0, N-1, 1, b-1, c)
    else:
        print(mult(0, N-1, 1, b-1, c-1))