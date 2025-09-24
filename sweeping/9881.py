import sys

n = int(input())

answer = 0

hills = []
for _ in range(n):
    hills.append(int(sys.stdin.readline()))

if n == 1:
    print(0)
    exit()

hills.sort()

lowest, highest = hills[0], hills[n-1]

difference = highest - lowest

lower = 0
higher = 0

if difference <= 17:
    print(0)
else:
    answer = float('inf')
    for i in range(lowest, min(highest+1, 84)):
        start = i
        end = i + 17
        temp = 0
        for hill in hills:
            if hill < start:
                temp += (start - hill) ** 2
            elif hill > end:
                temp += (hill - end) ** 2
        answer = min(answer, temp)
    print(answer)