from collections import deque
N, M = map(int, input().split())

board = []

red = None
blue = None
for i in range(N):
    row = list(input())
    if red == None or blue == None:
        for j in range(M):
            if row[j] == 'R':
                red = (i, j)
                row[j] = "."
            if row[j] == 'B':
                blue = (i, j)
                row[j] = '.'
    board.append(row)

q = deque([(red, blue, 0)])

visited = set()

while q:
    r, b, d = q.popleft()
    if d > 9:
        break
    r_y = r[0]
    r_x = r[1]
    b_y = b[0]
    b_x = b[1]

    if (r_y, r_x, b_y, b_x) in visited:
        continue
    
    visited.add((r_y,r_x, b_y, b_x))

    # 왼쪽 기울이기
    # 왼쪽에 있는 것 부터
    rx = r_x
    ry = r_y
    bx = b_x
    by = b_y
    if rx < bx: # red 부터
        isGoalIn = False
        for i in range(rx-1, -1, -1):
            if board[ry][i] == "#":
                rx = i + 1
                # red 공 위치에 임시 벽 생성
                board[ry][rx] = "#"
                break
            elif board[ry][i] == "O":
                isGoalIn = True
                break
            
        for i in range(bx-1, -1, -1):
            if board[by][i] == "#":
                if isGoalIn:
                    print(d+1)
                    exit()
                else:
                    bx = i + 1
                    board[ry][rx] = "."
                    q.append(((ry, rx), (by, bx), d+1))
                    break
            elif board[by][i] == 'O':
                board[ry][rx] = "."
                break
            
    else: # blue 부터
        isGoalIn = False
        for i in range(bx-1, -1, -1):
            if board[by][i] == "#":
                bx = i + 1
                # blue 공 위치에 임시 벽 생성
                board[by][bx] = "#"
                break
            elif board[by][i] == "O":
                isGoalIn = True
                break
        
        if not isGoalIn:
            for i in range(rx-1, -1, -1):
                if board[ry][i] == "#":
                    rx = i + 1
                    board[by][bx] = "."
                    q.append(((ry, rx), (by, bx), d+1))
                    break
                elif board[ry][i] == "O":
                    print(d+1)
                    exit()

    # 위쪽 기울이기
    rx = r_x
    ry = r_y
    bx = b_x
    by = b_y
    # 위쪽에 있는 것부터
    if ry < by: # red 부터
        isGoalIn = False
        for i in range(ry-1, -1, -1):
            if board[i][rx] == "#":
                ry = i + 1
                board[ry][rx] = "#"
                break
            elif board[i][rx] == "O":
                isGoalIn = True
                break

        for i in range(by-1, -1, -1):
            if board[i][bx] == "#":
                if isGoalIn:
                    print(d+1)
                    exit()
                else:
                    by = i + 1
                    board[ry][rx] = "."
                    q.append(((ry, rx), (by, bx), d + 1))
                    break
            elif board[i][bx] == "O":
                board[ry][rx] = "."
                break
                
    else: # blue 부터
        isGoalIn = False
        for i in range(by-1, -1, -1):
            if board[i][bx] == "#":
                by = i + 1
                board[by][bx] = "#"
                break
            elif board[i][bx] == "O":
                isGoalIn = True
                break

        if not isGoalIn:
            for i in range(ry-1, -1, -1):
                if board[i][rx] == "#":
                    ry = i + 1
                    board[by][bx] = "."
                    q.append(((ry, rx), (by, bx), d + 1))
                    break
                elif board[i][rx] == "O":
                    print(d+1)
                    exit()
        else:
            board[by][bx] = "."
        
    # 오른쪽 기울이기
    rx = r_x
    ry = r_y
    bx = b_x
    by = b_y
    # 오른쪽에 있는 것 부터
    if rx > bx: # red 부터
        isGoalIn = False
        for i in range(rx+1, M):
            if board[ry][i] == "#":
                rx = i-1
                board[ry][rx] = "#"
                break
            elif board[ry][i] == "O":
                isGoalIn = True
                break

        for i in range(bx+1, M):
            if board[by][i] == "#":
                if isGoalIn:
                    print(d+1)
                    exit()
                else:
                    bx = i - 1
                    board[ry][rx] = "."
                    q.append(((ry, rx), (by, bx), d + 1))
                    break
            elif board[by][i] == "O":
                board[ry][rx] = "."
                break
    else: # blue 부터
        isGoalIn = False
        for i in range(bx+1, M):
            if board[by][i] == "#":
                bx = i - 1
                board[by][bx] = "#"
                break
            elif board[by][i] == "O":
                isGoalIn = True
                break
        
        if not isGoalIn:
            for i in range(rx+1, M):
                if board[ry][i] == "#":
                    rx = i - 1
                    board[by][bx] = "."
                    q.append(((ry, rx), (by, bx), d + 1))
                    break
                elif board[ry][i] == "O":
                    print(d+1)
                    exit()

    # 아래쪽 기울이기
    rx = r_x
    ry = r_y
    bx = b_x
    by = b_y
    if ry > by: #red 부터
        isGoalIn = False
        for i in range(ry+1, N):
            if board[i][rx] == "#":
                ry = i - 1
                board[ry][rx] = "#"
                break
            elif board[i][rx] == "O":
                isGoalIn = True
                break
        
        for i in range(by+1, N):
            if board[i][bx] == "#":
                if isGoalIn:
                    print(d+1)
                    exit()
                else:
                    by = i - 1
                    board[ry][rx] = "."
                    q.append(((ry, rx), (by, bx), d+1))
                    break
            elif board[i][bx] == "O":
                board[ry][rx] = "."
                break
    else:
        isGoalIn = False
        for i in range(by+1, N):
            if board[i][bx] == "#":
                by = i - 1
                board[by][bx] = "#"
                break
            elif board[i][bx] == "O":
                isGoalIn = True
                break
        
        if not isGoalIn:
            for i in range(ry+1, N):
                if board[i][rx] == "#":
                    ry = i - 1
                    board[by][bx] = "."
                    q.append(((ry, rx), (by, bx), d+1))
                    break
                elif board[i][rx] == "O":
                    print(d+1)
                    exit()

print(-1)