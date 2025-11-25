answers = []

for _ in range(int(input())):
    h, w = map(int, input().split())
    board = []
    board.append(['*'] * (w+2))
    for _ in range(h):
        row = ['*']
        row.extend(list(input()))
        row.append('*')
        board.append(row)
    board.append(['*'] * (w+2))
    keys = set(input().upper())

    visited = [[False] * (w+2) for _ in range(h+2)]

    doors = dict()
    for i in range(65, 91):
        doors[chr(i)] = []

    q = []

    answer = 0

    def check(r, c):
        global answer
        if board[r][c] == '*':
            return
        elif board[r][c] == '.' or board[r][c] == '$':
            q.append((r, c))
        elif 64 < ord(board[r][c]) < 91:      # door
            if board[r][c] not in keys: # 현재 가진 키로 열 수 없으면 doors 에 임시 저장
                doors[board[r][c]].append((r, c))
            else:       # 현재 가진 키로 열 수 있으면 queue 로
                q.append((r, c))
        else:       # key
            # 습득한 열쇠로 열 수 있는 문이 있으면 해당 문의 좌표를 queue 로
            for door in doors[board[r][c].upper()]:
                q.append(door)
            doors[board[r][c].upper()].clear()
            keys.add(board[r][c].upper())
            q.append((r, c))

    # find entry
    for r in range(1, h+1):
        check(r, 1)
        check(r, w)
    for c in range(2, w):
        check(1, c)
        check(h, c)
    
    while q:
        r, c = q.pop()

        if visited[r][c]:
            continue
        
        visited[r][c] = True
        if board[r][c] == '$':
            answer += 1
        for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
            if not visited[nr][nc]:
                check(nr, nc)
    answers.append(answer)

for i in answers:
    print(i)