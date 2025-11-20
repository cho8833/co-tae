N, M = map(int, input().split())

board = []

board.append([-1] * (M+2))
for _ in range(N):
    row = [-1]
    row.extend(list(map(int, list(input()))))
    row.append(-1)
    board.append(row)
board.append([-1] * (M+2))
answer = [[0] * M for _ in range(N)]

graphSet = [[0] * M for _ in range(N)]

index = 1

countMap = dict()

visited = [[False] * (M+2) for _ in range(N+2)]
for i in range(1,N+1):
    for j in range(1,M+1):
        if board[i][j] == 0:
            count = 0
            q = [(i, j)]

            while q:
                r,c = q.pop()

                if visited[r][c]:
                    continue
                
                visited[r][c] = True
                count += 1
                graphSet[r-1][c-1] = index

                for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                    if board[nr][nc] == 0 and not visited[nr][nc]:
                        q.append((nr,nc))
            countMap[index] = count
            index += 1

for i in range(1,N+1):
    for j in range(1,M+1):
        if board[i][j] == 1:
            adj = set()
            
            for r, c in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if board[r][c] == 0:
                    adj.add(graphSet[r-1][c-1])
            
            result = 1
            for a in adj:
                result += countMap[a]
            answer[i-1][j-1] = result % 10

for i in range(N):
    print("".join(map(str, answer[i])))