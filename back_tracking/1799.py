N = int(input())

available = [[], []]

for r in range(N):
    row = list(map(int, input().split()))
    for c in range(len(row)):
        if row[c] == 1:
            if (r + c) % 2 == 0:
                available[0].append((r, c))
            else:
                available[1].append((r, c))

answer= [0, 0]


# graph[0] : 오른쪽 위 대각선 graph[1] : 왼쪽 아래 대각선
# graph[0] -> r + c
# graph[1] -> N - 1 - c + r
graph = [[False] * (2 * N - 1) for _ in range(2)]

def bt(b, count, idx):
    global answer
    
    answer[b] = max(count, answer[b])
    
    for i in range(idx, len(available[b])):
        r = available[b][i][0]
        c = available[b][i][1]
        if not graph[0][r+c] and not graph[1][N-1-c+r]:
            graph[0][r+c] = True
            graph[1][N-1-c+r] = True

            bt(b, count+1, i+1)

            graph[0][r+c] = False
            graph[1][N-1-c+r] = False

bt(0, 0, 0)
bt(1, 0, 0)
print(answer[0] + answer[1])