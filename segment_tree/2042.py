import sys

input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())

st = [0] * (4 * N)
data = []
for _ in range(N):
    data.append(int(input()))

def init(start, end, i):
    if start == end:
        st[i] = data[start]
    else:
        mid = (start + end) // 2
        st[i] = init(start, mid, i * 2) + init(mid + 1, end, i * 2 + 1)
    return st[i]

# start : 시작 인덱스
# end : 마지막 인덱스
# left, right : 구간 합을 구하고자 하는 범위
def sum(start, end, i, left, right):
    # 범위 밖에 있는 경우
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return st[i]
    mid = (start + end) // 2
    return sum(start, mid, i * 2, left, right) + sum(mid+1, end, i * 2 + 1, left, right)

def update(start, end, i, target, value):
    if target < start or target > end:
        return
    st[i] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, i * 2, target, value)
    update(mid + 1, end, i * 2 + 1, target, value)

init(0, N-1, 1)

for _ in range(M + K):
    a, b, c = map(int, input().rstrip().split())

    if a == 1:
        update(0, len(data)-1, 1, b-1, c-data[b-1])
        data[b-1] = c
    else:
        print(sum(0, len(data)-1, 1, b-1, c-1))