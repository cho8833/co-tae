import bisect

n, m = map(int, input().split())

heights = list(map(int, input().split()))
heights.sort()

left, right = 0, heights[-1]
answer = 0
while left+1 < right:
    height = (left + right) // 2

    mid = bisect.bisect_left(heights, height)
    answer = 0
    for i in range(mid, n):
        answer += heights[i] - height
    
    if answer < m:
        right = height
    else:
        left = height

print(left)
