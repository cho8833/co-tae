N = int(input())

D = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (1 << N) for _ in range(N)]

# init
for i in range(N):
    dp[0][1 << i] = D[i][0] / 100

for i in range(N-1):
    for state in range(1 << N):
        if dp[i][state] > 0:
            for n in range(N):
                if state & 1 << n == 0:
                    next = state | 1 << n
                    dp[i+1][next] = max(dp[i+1][next], dp[i][state] * D[n][i+1] / 100)

print(dp[N-1][(1 << N) - 1] * 100)