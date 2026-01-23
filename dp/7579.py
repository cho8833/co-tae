N, M = map(int , input().split())

bytes = [0]
costs = [0]
bytes.extend(list(map(int , input().split())))
costs.extend(list(map(int, input().split())))

# dp[app number][max cost] = acc memory
dp = [[0] * (100 * N + 1) for _ in range(N + 1)]

answer = 10000

for n in range(1, N+1):

    for c in range(100 * N + 1):
        if c < costs[n]:
            dp[n][c] = dp[n-1][c]
        else:
            dp[n][c] = max(dp[n-1][c], dp[n-1][c-costs[n]] + bytes[n])
            if dp[n][c] >= M:
                answer = min(answer, c)

print(answer)