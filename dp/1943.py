for _ in range(3):
    N = int(input())
    coins = []
    total = 0
    for _ in range(N):
        v, k = map(int, input().split())
        total += v*k
        i = 1
        while k > 0:
            m = min(i , k)
            coins.append(v * m)
            k -= m
            i = i << 1
    
    if total % 2 == 1:
        print(0)
        continue
    
    target = total // 2

    if min(coins) > target:
        print(0)
        continue
    
    dp = [0] * (target+1)
    
    dp[0] = 1
    
    for c in range(len(coins)):
        coin = coins[c]
        for m in range(target, coin-1, -1):
            if dp[m-coin] == 1:
                dp[m] = 1
    print(dp[target])