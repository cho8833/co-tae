import copy
N = int(input())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))


def swipe(direction):
    newBoard = [[0] * N for _ in range(N)]
    if direction == 0:  # 오른쪽
        for r in range(N):
            temp = None
            boardCol = N-1
            for c in range(N-1, -1, -1):
                v = board[r][c]
                if v == 0:
                    continue
                if temp != v:
                    if temp == None:
                        temp = v
                    else:
                        newBoard[r][boardCol] = temp
                        boardCol -= 1
                        temp = v
                else:
                    newBoard[r][boardCol] = temp * 2
                    boardCol -= 1
                    temp = None
            if temp != None:
                newBoard[r][boardCol] = temp

    elif direction == 1:   # 왼쪽
        for r in range(N):
            temp = None
            boardCol = 0
            for c in range(N):
                v = board[r][c]
                if v == 0:
                    continue
                if temp != v:
                    if temp == None:
                        temp = v
                    else:
                        newBoard[r][boardCol] = temp
                        boardCol += 1
                        temp = v
                else:
                    newBoard[r][boardCol] = temp * 2
                    boardCol += 1
                    temp = None
            if temp != None:
                newBoard[r][boardCol] = temp
    elif direction == 2:    # 위쪽
        for c in range(N):
            temp = None
            boardRow = 0

            for r in range(N):
                v = board[r][c]
                if v == 0:
                    continue
                if temp != v:
                    if temp != None:
                        newBoard[boardRow][c] = temp
                        boardRow += 1
                    temp = v
                else:
                    newBoard[boardRow][c] = temp * 2
                    boardRow += 1
                    temp = None
            if temp != None:
                newBoard[boardRow][c] = temp
    
    elif direction == 3:   # 아래쪽
        for c in range(N):
            temp = None
            boardRow = N - 1

            for r in range(N-1, -1, -1):
                v = board[r][c]
                if v == 0:
                    continue
                if temp != v:
                    if temp != None:
                        newBoard[boardRow][c] = temp
                        boardRow -= 1
                    temp = v
                else:
                    newBoard[boardRow][c] = temp * 2
                    boardRow -= 1
                    temp = None
            if temp != None:
                newBoard[boardRow][c] = temp

    return newBoard

answer = 0

def bt(count):
    global answer
    global board
    if count == 5:
        answer = max(answer, max(map(max, board)))
        return
    
    temp = copy.deepcopy(board)
    for i in range(4):
        board = swipe(i)
        bt(count+1)
        board = copy.deepcopy(temp)
bt(0)
print(answer)