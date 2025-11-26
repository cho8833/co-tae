N = int(input())

# dp[자리수][n 으로 끝나는][bit mask]
dp = [[[0] * ((1 << 10)) for _ in range(10)] for _ in range(N)]

# 1자리 수
for n in range(1, 10):
    dp[0][n][1 << n] = 1

for n in range(N-1):  # n 자리
    for c in range(10): # c 로 끝나는
        for b in range(1, 1024):
           if c > 0:
               dp[n+1][c-1][b | (1 << (c-1))] += dp[n][c][b]
           if c < 9:
               dp[n+1][c+1][b | (1 << (c+1))] += dp[n][c][b]

answer = 0
for c in range(10):
    answer += dp[N-1][c][1023] 
print(answer % 1_000_000_000)

