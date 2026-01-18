N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * N for _ in range(N)]

def loop(r, c):
    if dp[r][c] != -1:
        return dp[r][c]
    

    hasNext = False
    for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
        if nr > N-1 or nr < 0 or nc > N-1 or nc < 0:
            continue
        if board[nr][nc] > board[r][c]:
            hasNext = True
            dp[r][c] = max(dp[r][c], loop(nr, nc) + 1)
    if not hasNext:
        dp[r][c] = 0
    
    return dp[r][c]

answer = 0     
for i in range(N):
    for j in range(N):
        if dp[i][j] == -1:
            answer = max(loop(i, j), answer)

print(answer+1)