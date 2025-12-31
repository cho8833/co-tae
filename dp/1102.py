N = int(input())

cost = []

for _ in range(N):
    cost.append(list(map(int, input().split())))

state = 0

temp = input()

count = 0

for i in range(N):
    if temp[i] == "Y":
        state += 1 << i
        count += 1

target = int(input())

if count >= target:
    print(0)
    exit()

if count == 0:
    print(-1)
    exit()
    
dp = [[float('inf')] * (1 << N) for _ in range(target+1)]

dp[count][state] = 0

for c in range(count, target):
    for state in range(1 << N):
        if dp[c][state] != float('inf'):
            for i in range(N):
                if state & 1 << i == 0:
                    for j in range(N):
                        if state & 1 << j > 0:
                            dp[c+1][state | 1 << i] = min(dp[c+1][state | 1 << i],dp[c][state] + cost[j][i])

print(min(dp[target]))