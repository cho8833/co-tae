import sys
import bisect
input = sys.stdin.readline

N = int(input())

pos = [int(input()) for _ in range(N)]

sortedPos = sorted(pos)

comp = [0] * N

# compress
for i in range(N):
    p = bisect.bisect_left(sortedPos, pos[i])
    comp[i] = p

seg = [0] * (4 * N)

def segSum(start, end, i, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return seg[i]
    
    mid = (start + end) // 2
    return segSum(start, mid, i * 2, left, right) + segSum(mid + 1, end, i * 2 + 1, left, right)


def update(start, end, i, target, val):
    if target < start or end < target:
        return
    seg[i] += val
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, i * 2, target, val)
    update(mid+1, end, i * 2 + 1, target, val)

for i in range(N):
    update(0, N-1, 1, comp[i], 1)
    print(i - segSum(0, N-1, 1, 0, comp[i]-1) + 1)
