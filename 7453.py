import sys

N = int(input())

A = []
B = []
C = []
D = []

for _ in range(N):
    a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = dict()

for i in range(N):
    for j in range(N):
        ab = A[i] + B[j]
        if ab in AB:
            AB[ab] += 1
        else:
            AB[ab] = 1

answer = 0

for i in range(N):
    for j in range(N):
        cd = C[i] + D[j]
        if -cd in AB:
            answer += AB[-cd]
print(answer)