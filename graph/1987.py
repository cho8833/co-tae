from collections import deque

R, C = map(int, input().split())

def bit(char):
    return 2**(ord(char) - 65)

board = []
board.append(['['] * (C+2))
for _ in range(R):
    row = ['[']
    row.extend(list(input()))
    row.append('[')
    board.append(row)
board.append(['['] * (C+2))

# bfs

queue = deque()

queue.append((1, 1, 1, bit('[')))

answer = 0

while queue:
    r, c, dist, alphabet = queue.pop()


    newBit =  alphabet | bit(board[r][c])

    if (newBit & bit(board[r+1][c])) == 0:
        queue.append((r+1, c, dist + 1, bit(board[r+1][c]) | newBit))

    if (newBit & bit(board[r-1][c])) == 0:
        queue.append((r-1, c, dist + 1, bit(board[r-1][c]) | newBit))

    if (newBit & bit(board[r][c+1])) == 0:
        queue.append((r, c+1, dist + 1,  bit(board[r][c+1]) | newBit))

    if (newBit & bit(board[r][c-1])) == 0:
        queue.append((r, c-1, dist + 1,  bit(board[r][c-1]) | newBit))
    
    answer = max(answer, dist)
print(answer)