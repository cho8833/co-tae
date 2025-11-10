import sys

answer = []

for _ in range(int(input())):
    n = int(sys.stdin.readline())

    board = []
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

    if n == 1:
        answer.append(max(board[0][0], board[1][0]))
        continue
    
    dp = [[0] * n for _ in range(2)]

    dp[0][0] = board[0][0]
    dp[1][0] = board[1][0]

    dp[0][1] = board[0][1] + board[1][0]
    dp[1][1] = board[0][0] + board[1][1]

    for i in range(2, n):
        dp[0][i] = max(dp[0][i-2], dp[1][i-2], dp[1][i-1]) + board[0][i]

        dp[1][i] = max(dp[0][i-2], dp[1][i-2], dp[0][i-1]) + board[1][i]
    
    answer.append(max(dp[0][n-1], dp[1][n-1], dp[0][n-2], dp[1][n-2]))

for a in answer:
    print(a)


