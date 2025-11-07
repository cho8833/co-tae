from collections import deque

N = int(input())

board = []

start = None

board.append([100] * (N+2))
for r in range(N):
    row = [100]
    row.extend(list(map(int, input().split())))
    for c in range(len(row)):
        if start == None:
            if row[c] == 9:
                start = (r+1, c)
                row[c] = 0
                break
    row.append(100)
    board.append(row)
board.append([100] * (N+2))

size = 2

eat = 0

answer = 0

moveQueue = deque()

moveQueue.append((start[0], start[1], 0))

# move queue
while moveQueue:

    r, c, t = moveQueue.popleft()

    board[r][c] = 0

    answer = t

    if eat == size:
        eat = 0
        size += 1

    # bfs
    queue = deque()
    visited = [[False] * (N+2) for _ in range(N+2)]
    queue.append((r, c, t))

    while queue:
        
        queue = deque(sorted(queue, key=lambda x:(x[2], x[0], x[1])))

        rt, ct, tt = queue.popleft()

        if visited[rt][ct]:
            continue

        if 0 < board[rt][ct] and board[rt][ct] < size:
            moveQueue.append((rt, ct, tt))
            eat += 1
            break
        
        visited[rt][ct] = True

        if not visited[rt-1][ct] and board[rt-1][ct] <= size:
            queue.append((rt-1, ct, tt+1))
        
        if not visited[rt][ct-1] and board[rt][ct-1] <= size:
            queue.append((rt, ct-1, tt+1))
        
        if not visited[rt][ct+1] and board[rt][ct+1] <= size:
            queue.append((rt, ct+1, tt+1))
            
        if not visited[rt+1][ct] and board[rt+1][ct] <= size:
            queue.append((rt+1, ct, tt+1))
        
print(answer)