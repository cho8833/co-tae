N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]

dp = [0] * (K+1)

for n in range(N):
    if coins[n] > K:
        continue
    coin = coins[n]
    dp[coin] = 1
    for k in range(coin+1, K+1):
        if dp[k-coin] > 0:
            if dp[k] == 0:
                dp[k] = dp[k-coin] + 1
            else:
                dp[k] = min(dp[k], dp[k-coin] + 1)
if dp[K] == 0:
    print(-1)
else:
    print(dp[K])