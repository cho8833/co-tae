N = int(input())

D = []

INF = 20 * 10000
for _ in range(N):
    D.append(list(map(int, input().split())))

dp = [[INF] * (1 << N) for _ in range(N)]

# init
for i in range(N):
    dp[0][1 << i] = D[i][0]
for j in range(N-1):
    # j 번째 일
    for i in range(1 << N):
        if dp[j][i] != INF:
            for p in range(N):
                if i & 1 << p == 0: # j+1 번째 일을 p 번 사람이 함
                    dp[j+1][i | 1 << p] = min(dp[j+1][i | 1 << p], dp[j][i] + D[p][j+1])
print(dp[N-1][-1])