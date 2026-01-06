import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

L = [int(input()) for _ in range(N)]

seg = [0] * (4 * N)

def init(start, end, i):
    if start == end:
        seg[i] = L[start]
    else:
        mid = (start + end) // 2
        seg[i] = min(init(start, mid, i * 2), init(mid+1, end, i * 2 + 1))
    return seg[i]

def segMin(start, end, i, left, right):
    if left > end or right < start:
        return 1_000_000_000
    if left <= start and right >= end:
        return seg[i]
    mid = (start + end) // 2
    return min(segMin(start, mid, i * 2, left, right), segMin(mid+1, end, i*2+1, left, right))

init(0, N-1, 1)

for _ in range(M):
    a, b= map(int, input().rstrip().split())
    print(segMin(0, N-1, 1, a-1, b-1))