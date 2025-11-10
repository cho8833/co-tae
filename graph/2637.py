from collections import deque

N, M = map(int, input().split())

board = []

board.append([-1] * (M+2))
for _ in range(N):
    row = [-1]
    row.extend(list(map(int, input().split())))
    row.append(-1)
    board.append(row)
board.append([-1] * (M+2))


def checkBoard():
    for i in range(1, N+1):
        for j in range(1, M+1):
            if board[i][j] > 0:
                return True
    return False

def cleanBoard():
    global board
    for i in range(1, N+1):
        for j in range(1, M+1):
            if board[i][j] > 2:
                board[i][j] = 0
            elif board[i][j] == 2:
                board[i][j] = 1

answer = 0    

while checkBoard():
    
    # bfs
    visited = [[False] * (M+2) for _ in range(N+2)]

    queue = deque()

    queue.append((1,1))

    while queue:
        r, c = queue.popleft()

        if visited[r][c]:
            continue
        
        visited[r][c] = True
        
        if not visited[r+1][c]:
            if board[r+1][c] == 0:
                queue.append((r+1, c))
            elif board[r+1][c] > 0:
                board[r+1][c] += 1
        
        if not visited[r-1][c]:
            if board[r-1][c] == 0:
                queue.append((r-1, c))
            elif board[r-1][c] > 0:
                board[r-1][c] += 1
        
        if not visited[r][c+1]:
            if board[r][c+1] == 0:
                queue.append((r, c+1))
            elif board[r][c+1] > 0:
                board[r][c+1] += 1
        
        if not visited[r][c-1]:
            if board[r][c-1] == 0:
                queue.append((r, c-1))
            elif board[r][c-1] > 0:
                board[r][c-1] += 1
    
    answer += 1
    cleanBoard()
print(answer)