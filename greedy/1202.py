import sys
import heapq

N, K = map(int, input().split())

jewels = []
for _ in range(N):
    M, V = list(map(int, sys.stdin.readline().rstrip().split()))
    heapq.heappush(jewels, (M, -V))

bags = []
for _ in range(K):
    heapq.heappush(bags, (int(sys.stdin.readline())))

answer = 0

jTemp = []

while bags:
    b = heapq.heappop(bags) 
    while jewels:
        if jewels[0][0] > b:
            break
        m, v = heapq.heappop(jewels)
        heapq.heappush(jTemp, v)

    # 가방에 맞는 보석이 없을 경우
    if not jTemp:
        continue
    else:
        v = heapq.heappop(jTemp)
        answer += -v
print(answer)