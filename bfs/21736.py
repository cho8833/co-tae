import sys
from collections import deque
n , m = map(int, input().split())

board = []

start = None
for i in range(n):
    row = list(sys.stdin.readline().rstrip())
    if start == None:
        for j in range(len(row)):
            if row[j] == "I":
                start = (i, j)
                break
    board.append(row)


answer = 0

queue = deque([start])

visited = [[False] * m for _ in range(n)]
visited[start[0]][start[1]] = True
while queue:
    pos = queue.pop()
    if board[pos[0]][pos[1]] == "P":
        answer += 1
    
    if pos[1] + 1 < m:
        if not visited[pos[0]][pos[1] + 1] and board[pos[0]][pos[1] + 1] != "X":
            queue.append((pos[0], pos[1] + 1))
            visited[pos[0]][pos[1]+ 1] = True

    if pos[0] + 1 < n:
        if not visited[pos[0]+1][pos[1]] and board[pos[0]+1][pos[1]] != "X":
            queue.append((pos[0]+1, pos[1]))
            visited[pos[0]+1][pos[1]] = True
    
    if pos[0] - 1 > -1:
        if not visited[pos[0]-1][pos[1]] and board[pos[0]-1][pos[1]] != "X":
            queue.append((pos[0]-1, pos[1]))
            visited[pos[0]-1][pos[1]] = True
    
    if pos[1] - 1 > -1:
        if not visited[pos[0]][pos[1]-1] and board[pos[0]][pos[1]-1] != "X":
            queue.append((pos[0], pos[1] - 1))
            visited[pos[0]][pos[1]-1] = True

if answer == 0:
    print("TT")
else:
    print(answer)