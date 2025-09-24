import sys

n, m = map(int, input().split())

tree = list(map(int, sys.stdin.readline().split()))

start = 0
end = int(1e9)
mid = 0
while start +1 < end:

    temp = 0
    mid = (start + end) // 2
    for i in range(n):
        cut = tree[i] - mid
        if cut > 0:
            temp += cut
    
    if temp <= m:
        end = mid
    else:
        start = mid

print(int(start))