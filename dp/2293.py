N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]

dp = [0] * (K + 1)

for n in range(N):
    if coins[n] > K:
        continue
    coin = coins[n]
    dp[coin] += 1                                          
    for k in range(1, K+1):
        if dp[k] > 0 and k + coin < K+1:
            dp[k + coin] += dp[k]
print(dp[K])