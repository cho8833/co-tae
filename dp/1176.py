N, K = map(int, input().split())

height = [int(input()) for _ in range(N)]

# dp[bit][kid] = count
dp = [[0] * N for _ in range(1 << N)]

# init
for i in range(N):
    dp[1 << i][i] = 1

for state in range(1 << N):
    for kid in range(N):
        if dp[state][kid] > 0:
            for n in range(N):
                if state & 1 << n == 0 and abs(height[kid] - height[n]) > K:
                    dp[state | 1 << n][n] += dp[state][kid]

print(sum(dp[(1 << N) - 1]))