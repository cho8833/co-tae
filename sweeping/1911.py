import sys

n,l = map(int, input().split())

pools = []
for _ in range(n):
    pools.append(list(map(int, sys.stdin.readline().split())))

pools.sort()

answer = 0

wEnd = 0
for i in range(n):
    pool = pools[i]
    start = pool[0]
    end = pool[1]

    # 현재 널빤지 끝부분이 start 보다 앞에 있는 경우
    if wEnd <= start:
        d, m = divmod(end-start, l)
        if m > 0:
            d += 1
        answer += d
        wEnd = start + l * d
    else:
        d, m = divmod(end-wEnd, l)
        if m > 0:
            d += 1
        answer += d
        wEnd = wEnd + l * d
print(answer)