N, M = map(int, input().split())

board = []

board.append([-1] * (M+2))
for _ in range(N):
    row = [-1]
    row.extend(list(map(int, input().split())))
    row.append(-1)
    board.append(row)
board.append([-1] * (M+2))

# 각 섬 위치 기록
islands = [[],[]]
island_num = 2

# 섬 번호 매기기
for i in range(1,N+1):
    for j in range(1,M+1):
        if board[i][j] == 1:

            island = []
            # dfs 로 섬 탐색
            q = [(i, j)]
            while q:
                r, c = q.pop()
                if board[r][c] != 1:
                    continue
                board[r][c] = island_num
                island.append((r, c))
                for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                    if board[nr][nc] == 1:
                        q.append((nr, nc))
            islands.append(island)
            island_num += 1
# graph 생성
graph = [[float('inf')] * island_num for _ in range(island_num)]
for i in range(2, len(islands)):
    island = islands[i]
    for l in range(len(island)):
        r, c = island[l] # 육지

        # 각 방향 검사 후 바다인 부분으로 진행
        for dr, dc in (1, 0), (-1, 0), (0, -1), (0, 1):
            # nr, nc : 현재 위치
            nr = r + dr
            nc = c + dc
            if board[nr][nc] == 0:
                if nr+dr > N or nr+dr < 1 or nc+dc > M or nc+dc < 1:
                    continue
                if board[nr+dr][nc+dc] == 0:
                    length = 2
                    nr += dr
                    nc += dc
                    while True:
                        # 한 칸 전진
                        nr += dr
                        nc += dc
                        if board[nr][nc] > 0 and board[nr][nc] != i:
                            graph[i][board[nr][nc]] = min(graph[i][board[nr][nc]], length)
                            break
                        elif board[nr][nc] == -1 or board[nr][nc] == i:
                            break
                        length += 1
                
parent = [i for i in range(island_num)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a
# 경로 정렬
paths = []
for r in range(2, island_num):
    for c in range(2, island_num):
        if graph[r][c] != float('inf'):
            paths.append((graph[r][c], r, c))
paths.sort()

answer = 0
for v, r, c in paths:
    if find(r) != find(c):
        union(r, c)
        answer += v

current = find(2)
for i in range(3, len(parent)):
    if current != find(i):
        print(-1)
        exit()

print(answer)