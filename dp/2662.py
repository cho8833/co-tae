N, M = map(int,input().split())

# invest[i][m] = i+1 원 투자헸을 때 m 기업의 투자금액
invest = []
for i in range(N):
    invest.append(list(map(int, input().split())))

# dp[기업 번호][투자 금액] = 이익
dp = [[0] * (N+1) for _ in range(M+1)]

# enterprise : 기업 번호 
# n : 투자 금액
for enterprise in range(1, M+1):
    for n in range(1,N+1):
        for i in range(n):
            # i+1 원 투자
            dp[enterprise][n] = max(dp[enterprise-1][n], dp[enterprise-1][n-(i+1)] + invest[i][enterprise], dp[enterprise][n])

print(dp[-1][-1])

# 역추적
answer = [0] * M

value = dp[M][N]
enterprise = M
current_invest = N
while value != 0:
    for i in range(N):
        if dp[enterprise][current_invest] == dp[enterprise-1][current_invest - (i+1)] + invest[i][enterprise]:
            value -= invest[i][enterprise]
            answer[enterprise-1] = i+1
            current_invest -= (i+1)
            break
    
    enterprise -= 1

print(*answer)