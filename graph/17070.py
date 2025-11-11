N = int(input())

board = []

board.append([-1] * (N+2))
for _ in range(N):
    row = [-1]
    row.extend(list(map(int, input().split())))
    row.append(-1)
    board.append(row)
board.append([-1] * (N+2))

if board[N][N] == 1:
    print(0)
    exit()

queue = []

queue.append((1, 2, 0))

answer = 0


while queue:
    r, c, state = queue.pop()

    if r == N and c == N:
        answer += 1
        continue

    # 가로
    if state == 0:
        # 가로 이동
        if board[r][c+1] == 0:
            queue.append((r, c+1, 0))

    # 대각선
    elif state == 1:
        # 가로 이동
        if board[r][c+1] == 0:
            queue.append((r, c+1, 0))
        # 세로 이동
        if board[r+1][c] == 0:
            queue.append((r+1, c, 2))

    # 세로
    else:
        # 세로 이동
        if board[r+1][c] == 0:
            queue.append((r+1, c, 2))
    
    # 대각선 이동
    if board[r+1][c+1] == 0 and board[r+1][c] == 0 and board[r][c+1] == 0:
        queue.append((r+1, c+1, 1))

print(answer)