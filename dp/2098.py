N = int(input())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

dp = [[float('inf')] * (2**N) for _ in range(N)]


q = [(0, 1)]
dp[0][1] = 0


while q:
    
    n, visited = q.pop()

    for adj in range(N):
        if matrix[n][adj] != 0 and visited & 1 << adj == 0: # n 에서 adj 까지 경로가 있으면 and 방문하지 않았으면
            adjVisit = visited | 1 << adj
            if dp[adj][adjVisit] > dp[n][visited] + matrix[n][adj]:
                dp[adj][adjVisit] = dp[n][visited] + matrix[n][adj]
                q.append((adj, adjVisit))

answer = float('inf')
for n in range(1, N):
    if matrix[n][0] != 0:
        answer = min(answer, dp[n][-1] + matrix[n][0])
print(answer)