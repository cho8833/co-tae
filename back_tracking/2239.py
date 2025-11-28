board = []

for _ in range(9):
    board.append(list(map(int, list(input()))))
rows = [set(list(range(1,10))) for _ in range(9)]

cols = [set(list(range(1, 10))) for _ in range(9)]

squares = [set(list(range(1, 10))) for _ in range(9)]

for i in range(9):
    for j in range(9):
        if board[i][j] > 0:
            rows[i].remove(board[i][j])
            squares[3 * (i // 3) + (j // 3)].remove(board[i][j])
        if board[j][i] > 0:
            cols[i].remove(board[j][i])

def check():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True

def bt(r):
    # 다 채워졌는지 확인
    if check():
       for i in range(9):
           print("".join(map(str, board[i]))) 
       exit()


    for i in range(r, 9):
        for j in range(9):
            if board[i][j] == 0:
                available = rows[i] & cols[j] & squares[3 * (i // 3) + (j // 3)]
                if len(available) == 0:
                    return
                for a in sorted(list(available)): # 사전식으로 앞서기 위해 sort
                    rows[i].remove(a)
                    cols[j].remove(a)
                    squares[3 * (i // 3) + (j // 3)].remove(a)
                    board[i][j] = a

                    bt(i)

                    rows[i].add(a)
                    cols[j].add(a)
                    squares[3 * (i // 3) + (j // 3)].add(a)
                    board[i][j] = 0
                return

bt(0)