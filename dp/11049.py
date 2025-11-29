N = int(input())

matrix = []

for _ in range(N):
    r, c = map(int, input().split())
    matrix.append((r, c))

dp = [[float(float('inf'))] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 0


def recur(count):
    if count == N:
        return
    for i in range(N-count):
        for t in range(count):
            dp[i][i+count] = min(dp[i][i+count], dp[i][i+t] + dp[i+t+1][i+count] + matrix[i][0] * matrix[i+t][1] * matrix[i+count][1])
    recur(count + 1)

recur(1)

print(dp[0][N-1])