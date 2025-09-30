from collections import deque

n, m = map(int, input().split())

board = []
visited = [[-1] * m for _ in range(n)]

sc = 0
sr = 0
for c in range(n):
    row = list(map(int, input().split()))
    for r in range(m):
        if row[r] == 0:
            visited[c][r] = 0
        elif row[r] == 2:
            sc = c
            sr = r
    board.append(row)

for c in range(n):
    for r in range(m):
        if board[c][r] == 0:
            visited[c][r] = 0

queue = deque([(sc, sr, 0)])
while queue:
    c, r, dist = queue.popleft()

    if visited[c][r] != -1:
        continue
    
    visited[c][r] = dist
    nextDist = dist+1

    if c > 0:
        if board[c-1][r] == 1:
            queue.append((c-1, r, nextDist))
    if c < n-1:
        if board[c+1][r] == 1:
            queue.append((c+1, r, nextDist))
    if r > 0:
        if board[c][r-1] == 1:
            queue.append((c, r-1, nextDist))
    if r < m-1:
        if board[c][r+1] == 1:
            queue.append((c, r+1, nextDist))

for col in visited:
    print(" ".join(list(map(str, col))))