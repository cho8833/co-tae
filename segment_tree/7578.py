N = int(input())

A = list(map(int, input().split()))

B = list(map(int , input().split()))

# 정리
idx = [0] * N

idxMap = dict()
for i in range(N):
    idxMap[A[i]] = i
for i in range(N):
    idx[i] = idxMap[B[i]]

seg = [0] * (4 * N)

def update(start, end, i, target, val):
    if target < start or target > end:
        return
    seg[i] += val
    if start == end:
        return
    mid = (start + end) // 2

    update(start, mid, i * 2, target, val)
    update(mid + 1, end, i * 2 + 1, target, val)

def segSum(start, end, i, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return seg[i]
    
    mid = (start + end) // 2
    return segSum(start, mid, i * 2, left, right) + segSum(mid+1, end, i* 2 + 1, left, right)

answer = 0

for i in range(N):
    answer += segSum(0, N - 1, 1, idx[i] + 1, N - 1)
    update(0, N-1, 1, idx[i], 1)
print(answer)