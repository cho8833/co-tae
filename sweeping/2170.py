import sys
n = int(input())

data = []

for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

data.sort()

cStart = data[0][0]
cEnd = data[0][1]
answer = cEnd - cStart

for i in range(1, len(data)):
    line = data[i]
    end = line[1]
    start = line[0]

    # 현재 끝 부분에서 벗어나는경우
    if start >= cEnd:
        cStart = start
        cEnd = end
        answer += cEnd - cStart
    
    # 걸쳐서 벗어난 경우
    elif end > cEnd:
        answer += end - cEnd
        cEnd = end

print(answer)