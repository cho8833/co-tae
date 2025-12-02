import sys
R, C, M = map(int, input().split())

sharks = []

board = [[-1] * C for _ in range(R)]


directions = [None, (-1, 0), (1, 0), (0, 1), (0, -1)]

for i in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().rstrip().split())
    if d == 1 or d == 2:
        s %= (R-1) * 2
    else:
        s %= (C-1) * 2
    sharks.append((r-1,c-1,s,d,z))
    board[r-1][c-1] = i

answer = 0
for c in range(C):
    newBoard = [[-1] * C for _ in range(R)]
    # 낚시
    for r in range(R):
        if board[r][c] != -1:
            answer += sharks[board[r][c]][4]
            board[r][c] = -1
            break
    

    # 상어 이동
    for i in range(M):
        shark = sharks[i]
        if board[shark[0]][shark[1]] != i:
            continue
        
        d = shark[3]
        mr, mc = directions[d]

        mr *= shark[2]
        mc *= shark[2]


        nr = shark[0] + mr

        nc = shark[1] + mc

        if nr > R-1:
            dChange, nr = divmod(nr, R-1)
            if dChange == 1:
                d = 1
                nr = R-1 - nr
        elif nr < 0:
            dChange, nr = divmod(abs(nr), R-1)
            if dChange == 0:
                d = 2
            elif dChange == 1:
                nr = R-1 - nr

        if nc > C-1:
            dChange, nc = divmod(nc, C-1)
            if dChange == 1:
                d = 4
                nc = C-1 - nc
        elif nc < 0:
            dChange, nc = divmod(abs(nc), C-1)
            if dChange == 0:
                d = 3
            elif dChange == 1:
                nc = C-1-nc

        if newBoard[nr][nc] != -1:
            if sharks[newBoard[nr][nc]][4] < shark[4]:
                newBoard[nr][nc] = i
                sharks[i] = (nr, nc, shark[2], d, shark[4])
                
        else:
            newBoard[nr][nc] = i
            sharks[i] = (nr, nc, shark[2], d, shark[4])

    board = newBoard

print(answer)