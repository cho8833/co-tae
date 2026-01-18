import sys
input = sys.stdin.readline

N = 1000000
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

def get(start, end, i, target):
    seg[i] -= 1
    if start == end:
        return start
    mid = (start + end) // 2
    if seg[i * 2] >= target:
        return get(start, mid, i * 2, target)
    else:
        return get(mid + 1, end, i * 2 + 1, target - seg[i * 2])
    

for _ in range(int(input())):
    ABC = list(map(int, input().rstrip().split()))

    if ABC[0] == 2:
        update(0, N, 1, ABC[1], ABC[2])
    else:
        print(get(0, N, 1, ABC[1]))

