import sys
import heapq
from collections import deque

N, K = map(int, input().split())

jewels = []
for _ in range(N):
    M, V = map(int, sys.stdin.readline().rstrip().split())
    jewels.append((M, -V))

bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline()))

jewels.sort()
bags.sort()

answer = 0

jTemp = []

jewels = deque(jewels)
bags = deque(bags)

while bags:
    b = bags.popleft()

    while jewels:
        if jewels[0][0] > b:
            break
        m, v = jewels.popleft()
        
        heapq.heappush(jTemp, v)

    # 가방에 맞는 보석이 없을 경우
    if not jTemp:
        continue
    else:
        v = heapq.heappop(jTemp)
        answer += -v
print(answer)