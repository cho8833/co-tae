N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

direction = [0, 7,3,1,5]

data = [0] * N ** 2

answer = 0

def init():
    i = N ** 2 - 1
    rStart, rEnd = 0, N-1
    cStart, cEnd = 0, N-1

    while i > 0:
        for c in range(cStart, cEnd):
            data[i] = board[rStart][c]
            i -= 1
        for r in range(rStart, rEnd):
            data[i] = board[r][cEnd]
            i -= 1
        for c in range(cEnd, cStart, -1):
            data[i] = board[rEnd][c]
            i -= 1
        for r in range(rEnd, rStart, - 1):
            data[i] = board[r][cStart]
            i -= 1
        rStart += 1
        rEnd -= 1
        cStart += 1
        cEnd -= 1

init()

def blizzard(d, s):
    dir = direction[d]
    t = 0
    for i in range(s):
        t += dir + i * 8
        if data[t] == 0:
            break
        data[t] = -1

def push():
    global data
    temp = [0] * N ** 2
    i = 1
    j = 1
    while i < N ** 2:
        if data[i] == 0:
            break
        elif data[i] != -1:
            temp[j] = data[i]
            j += 1
        i += 1
    data = temp

def explode():
    global answer
    isExplode = False
    current = 0
    count = 1
    start = 0
    for i in range(1, N**2):
        if data[i] == current:
            count += 1
        else:
            if count > 3:
                isExplode = True
                for j in range(start, start + count):
                    data[j] = -1
                answer += current * count

            count = 1
            current = data[i]
            start = i
    return isExplode

def mutate():
    global data
    temp = [0] * N ** 2
    count = 1
    current = data[1]
    j = 1
    for i in range(2, N ** 2):
        if data[i] == current:
            count += 1
        else:
            if j > N ** 2 - 1 or j + 1 > N ** 2 - 1:
                break
            temp[j] = count
            temp[j+1] = current
            count = 1
            current = data[i]
            j += 2
    data = temp
for _ in range(M):
    d, s = map(int, input().split())

    blizzard(d, s)
    push()

    while explode():
        push()

    mutate()

print(answer)