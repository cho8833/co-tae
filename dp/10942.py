import sys
N = int(input())

S = list(map(int, input().split()))

M = int(input())

dp = [[None] * N for _ in range(N)]

for i in range(N-2):
    dp[i][i] = True
    if S[i] == S[i+1]:
        dp[i][i+1] = True
    if S[i] == S[i+2]:
        dp[i][i+2] = True
dp[N-2][N-2] = True
if S[N-2] == S[N-1]:
    dp[N-2][N-1] = True
dp[N-1][N-1] = True

def isPal(i, j):
    if dp[i][j] != None:
        return dp[i][j]
    
    if i > j:
        return True
    if S[i] == S[j]:
        return isPal(i+1, j-1)
    else:
        return False

for i in range(N):
    for j in range(i+1):
        dp[j][i] = isPal(j, i)
        

for _ in range(M):
    s, e = map(int, sys.stdin.readline().rstrip().split())

    if dp[s-1][e-1]:
        print(1)
    else:
        print(0)