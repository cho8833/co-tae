N = int(input())

seq = list(map(int, input().split()))

answer = 1

incDP = [1] * N

decDP = [1] * N

#incDP
for i in range(N):
    for j in range(i-1, -1, -1):
        if seq[j] < seq[i]:
            incDP[i] = max(incDP[i], incDP[j] + 1)

for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if seq[j] < seq[i]:
            decDP[i] = max(decDP[i], decDP[j] + 1)

for i in range(N):
    answer = max(incDP[i] + decDP[i] - 1, answer)
print(answer)