N = int(input())

answer = [[False] * (N // 3 * 5 + (N//3 - 1)) for _ in range(N)]

def recur(y, x, n):
    if n == 3:
        for Y, X in (y,x), (y+1,x-1), (y+1,x+1), (y+2,x-2), (y+2,x-1), (y+2,x), (y+2,x+1), (y+2,x+2):
            answer[Y][X] = True
        return
    next = n // 2
    recur(y, x, next)
    recur(y + next, x - next, next)
    recur(y + next, x + next, next)

recur(0, N - 1, N)

for i in range(len(answer)):
    for j in range(len(answer[i])):
        print("*", end="") if answer[i][j] else print(" ", end="")
    print()