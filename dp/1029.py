N = int(input())
MAX = 20
price = [list(map(int, input())) for _ in range(N)]

# dp[state][owner] = price
dp = [[MAX] * 15 for _ in range(1 << N)]

# init
dp[1][0] = 0

answer = 0

for state in range(1, 1 << N):
    for owner in range(N):
        if dp[state][owner] < 10:
            answer = max(answer, format(state, 'b').count('1'))
            for n in range(N):
                if state & 1 << n == 0 and price[owner][n] >= dp[state][owner]:
                    nextState = state | 1 << n
                    dp[nextState][n] = min(dp[nextState][n], price[owner][n])

print(answer)