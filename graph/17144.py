R, C, T = map(int, input().split())

board = []

board.append([-2] * (C+2))
for _ in range(R):
    row = [-2]
    row.extend(list(map(int, input().split())))
    row.append(-2)
    board.append(row)
board.append([-2] * (C+2))

up = None
down = None

answer = 0

# find fresher
for i in range(1, R+1):
    if board[i][1] == -1:
        up = i
        break
for i in range(R, 0, -1):
    if board[i][1] == -1:
        down = i
        break

for _ in range(T):
    # create new board
    newBoard = []
    newBoard.append([-2] * (C+2))
    for _ in range(R):
        row = [-2]
        row.extend([0] * C)
        row.append(-2)
        newBoard.append(row)
    newBoard.append([-2] * (C+2))

    total = 0

    # diffusion
    for r in range(1, R+1):
        for c in range(1, C+1):
            if board[r][c] == -1:
                newBoard[r][c] = -1
                continue
            if board[r][c] > 4:
                diffusion = board[r][c] // 5
                count = 0
                for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                    if board[nr][nc] > -1:
                        count += 1
                        newBoard[nr][nc] += diffusion
                remain = board[r][c] - (count * diffusion)
                newBoard[r][c] += remain
            else:
                newBoard[r][c] += board[r][c]
            
            total += board[r][c]
    
    # refresh 미리 계산
    total -= newBoard[up-1][1]
    total -= newBoard[down+1][1]

    # refresh
        # up
    for r in range(up-1, 0, -1):
        newBoard[r][1], newBoard[r+1][1] = newBoard[r+1][1], newBoard[r][1]
    newBoard[up][1] = 0
    for c in range(1, C):
        newBoard[1][c], newBoard[1][c+1] = newBoard[1][c+1], newBoard[1][c]
    for r in range(1, up):
        newBoard[r][C], newBoard[r+1][C] = newBoard[r+1][C], newBoard[r][C]
    for c in range(C, 1, -1):
        newBoard[up][c], newBoard[up][c-1] = newBoard[up][c-1], newBoard[up][c]
    

        # down
    for r in range(down, R):
        newBoard[r][1], newBoard[r+1][1] = newBoard[r+1][1], newBoard[r][1]
    newBoard[down][1] = 0
    for c in range(1, C):
        newBoard[R][c], newBoard[R][c+1] = newBoard[R][c+1], newBoard[R][c]
    for r in range(R, down, -1):
        newBoard[r][C], newBoard[r-1][C] = newBoard[r-1][C], newBoard[r][C]
    for c in range(C, 1, -1):
        newBoard[down][c], newBoard[down][c-1] = newBoard[down][c-1], newBoard[down][c]
    
    
    board = newBoard

    answer = total
print(answer)