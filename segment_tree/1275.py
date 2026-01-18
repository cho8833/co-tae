import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
data = list(map(int, input().rstrip().split()))


seg = [0] * (4*N)

def init(start, end, i):
    if start == end:
        seg[i] = data[start]
    else:
        mid = (start + end) // 2
        seg[i] = init(start, mid, i * 2) + init(mid+1, end, i*2+1)
    return seg[i]

def segSum(start, end, i, left, right):
    if left > end or start > right:
        return 0
    if left <= start and right >= end:
        return seg[i]
    mid = (start + end) // 2
    return segSum(start, mid, i * 2, left, right) + segSum(mid+1, end, i * 2 + 1, left, right)

def update(start, end, i, target, val):
    if target < start or target > end:
        return
    seg[i] += val
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, i*2, target, val)
    update(mid+1, end, i*2+1, target, val)

init(0, N-1, 1)

for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if y < x:
        x, y = y, x
    print(segSum(0, N-1, 1, x-1, y-1))
    diff = b  - data[a-1]
    data[a-1] = b
    update(0, N-1, 1, a-1, diff)