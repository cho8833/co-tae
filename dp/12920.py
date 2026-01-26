N, M = map(int, input().split())

# stuffs = [(무게, 만족도), ....]
stuffs = [()]

for i in range(N):
    v, c, k = map(int, input().split())

    i = 1
    while k > 0:
        m = min(k, i)
        stuffs.append((v * m, c * m))
        k -= m
        i = i << 1

# dp[물건 번호][최대 무게] = 만족도
dp = [[0] * (M + 1) for _ in range(len(stuffs))]

for n in range(1, len(stuffs)):
    for m in range(1, M+1):
        v, c = stuffs[n]
        if v > m:
            dp[n][m] = dp[n-1][m]
        else:
            dp[n][m] = max(dp[n-1][m], dp[n-1][m-v] + c)

print(dp[-1][-1])