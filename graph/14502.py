from collections import deque
N, M = map(int, input().split())

board = []
board.append([-1] * (M+2))

viruses = []


for j in range(N):
    row = [-1]
    row.extend(list(map(int, input().split())))    
    row.append(-1)

    for i in range(1, M+1):
        if row[i] == 2:
            viruses.append((j+1, i))
    
    board.append(row)
board.append([-1] * (M+2))

answer = 0

def bfs():
    global answer
    queue = deque(viruses)

    visited = []
    visited.append([True] * (M+2))
    for _ in range(N):
        row = [True]
        row.extend([False] * (M))
        row.append(True)
        visited.append(row)
    visited.append([True] * (M+2))

    for i in range(1, N+1):
        for j in range(1, M+1):
            if board[i][j] == 1:
                visited[i][j] = True
    
    while queue:
        r, c = queue.popleft()

        if visited[r][c]:
            continue
        
        visited[r][c] = True

        for nr, nc in (r+1, c), (r, c+1), (r-1, c), (r, c-1):
            if not visited[nr][nc] and board[nr][nc] == 0:
                queue.append((nr,nc))
    
    result = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if not visited[i][j]:
                result += 1
    
    answer = max(answer, result)


def wall(count):
    if count == 3:
        bfs()
        return
    
    for i in range(1, N+1):
        for j in range(1, M+1):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(count + 1)
                board[i][j] = 0

wall(0)

print(answer)