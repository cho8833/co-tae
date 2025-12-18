import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

maxT = [0] * (4 * N)

minT = [0] * (4 * N)

data = []

for _ in range(N):
    data.append(int(input()))

def initMax(start, end, i):
    if start == end:
        maxT[i] = data[start]
    else:
        mid = (start + end) // 2
        maxT[i] = max(initMax(start, mid, i * 2), initMax(mid+1, end, i * 2 + 1))
    return maxT[i]

def initMin(start, end, i):
    if start == end:
        minT[i] = data[start]
    else:
        mid = (start + end) // 2
        minT[i] = min(initMin(start, mid, i * 2), initMin(mid + 1, end, i * 2 + 1))
    return minT[i]

def maxTree(start, end, i , left, right):
    if left > end or start > right:
        return 0
    if left <= start and right >= end:
        return maxT[i]
    mid = (start + end) // 2
    return max(maxTree(start, mid, i * 2, left, right), maxTree(mid + 1, end, i * 2 + 1, left, right))

def minTree(start, end, i , left, right):
    if left > end or start > right:
        return float('inf')
    if left <= start and right >= end:
        return minT[i]
    mid = (start + end) // 2
    return min(minTree(start, mid, i * 2, left, right), minTree(mid + 1, end, i * 2 + 1, left, right))

initMax(0, N-1, 1)
initMin(0, N-1, 1)

for _ in range(M):
    a, b = map(int ,input().rstrip().split())

    print(minTree(0, N-1, 1, a-1, b-1), maxTree(0, N-1, 1, a-1, b-1))