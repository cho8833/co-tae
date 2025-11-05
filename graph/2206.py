import sys
from collections import deque


N, M = map(int, input().split())


board = []

board.append([-1] * (M+2))
for i in range(N):
    row = [-1]
    row.extend(map(int, list(sys.stdin.readline().rstrip())))
    row.append(-1)
    board.append(row)
board.append([-1] * (M+2))

queue = deque()

queue.append((1,1, 1, 0))

visited = [[[False] * (M+2) for _ in range(N+2)] for _ in range(2)]

answer = -1

while queue:
    i, j, dist, broke = queue.popleft()

    if i == N and j == M:
        print(dist)
        exit()

    if visited[broke][i][j]:
        continue
    
    visited[broke][i][j] = True

    if broke == 1:
        if board[i][j+1] == 0 and not visited[1][i][j+1]:
            queue.append((i, j+1, dist+1, True))
        if board[i][j-1] == 0 and not visited[1][i][j-1]:
            queue.append((i, j-1, dist+1, True))
        if board[i+1][j] == 0 and not visited[1][i+1][j]:
            queue.append((i+1, j, dist+1, True))
        if board[i-1][j] == 0 and not visited[1][i-1][j]:
            queue.append((i-1, j, dist+1, True))
    else:
        if not visited[0][i][j+1]:
            if board[i][j+1] == 1:
                queue.append((i, j+1, dist+1, True))
            elif board[i][j+1] == 0:
                queue.append((i, j+1, dist+1, False))
        if not visited[0][i][j-1]:
            if board[i][j-1] == 1:
                queue.append((i, j-1, dist+1, True))
            elif board[i][j-1] == 0:
                queue.append((i, j-1, dist+1, False))
        if not visited[0][i+1][j]:
            if board[i+1][j] == 1:
                queue.append((i+1, j, dist+1, True))
            elif board[i+1][j] == 0:
                queue.append((i+1, j, dist+1, False))
        if not visited[0][i-1][j]:
            if board[i-1][j] == 1:
                queue.append((i-1, j, dist+1, True))
            elif board[i-1][j] == 0:
                queue.append((i-1, j, dist+1, False))


print(-1)