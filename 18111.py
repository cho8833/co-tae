import sys

N, M, B = map(int, input().split())

ground = []

minHeight = 257
maxHeight = 0
for i in range(N):
    ground.append(list(map(int, sys.stdin.readline().rstrip().split())))
    tMin = min(ground[i])
    tMax = max(ground[i])
    minHeight = min(tMin, minHeight)
    maxHeight = max(tMax, maxHeight)

answer = 1e9
answer_height = 0

for height in range(maxHeight, minHeight-1, -1):
    time = 0
    tB = B
    for i in range(N):
        for j in range(M):
            if ground[i][j] <= height:
                required = height - ground[i][j]
                tB -= required
                time += required
            else:
                remove = ground[i][j] - height
                tB += remove
                time += (remove * 2)
    if tB >= 0 and answer > time:
        answer = time
        answer_height = height
print(answer, answer_height)
