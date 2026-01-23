for _ in range(int(input())):
    N = int(input())

  
    coins = list(map(int, input().split()))
    M = int(input())

    # dp[coin number][max M] = count
    dp = [[0] * (M+1) for _ in range(N)]

    for n in range(N):
        dp[n][0] = 1

    # init
    i = 1
    while (coins[0] * i <= M):
        dp[0][coins[0] * i] = 1
        i += 1
    
    for n in range(1, N):
        coin = coins[n]
        # dp[n][coin] += 1
        for m in range(1,M+1):
            if coin > m:
                dp[n][m] += dp[n-1][m]
            else:
                dp[n][m] += dp[n-1][m] + dp[n][m-coin]
    print(dp[-1][M])