import sys

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(sys.stdin.readline()))


house.sort()

answer = 0

start = 1
end = house[-1] - house[0] + 1

while start + 1 < end:
    mid = (start + end) // 2
    
    current = house[0]
    count = 1
    for i in range(1, len(house)):
        if house[i] >= current + mid:
            count += 1
            current = house[i]
    
    if count < c:
        end = mid
    else:
        start = mid

print(start)
