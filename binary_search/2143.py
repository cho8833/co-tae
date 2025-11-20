import bisect

T = int(input())
n = int(input())
A = list(map(int , input().split()))
m = int(input())
B = list(map(int, input().split()))

answer = 0

aSub = dict()
for i in range(n):
    pSum = 0
    for j in range(i, n):
        pSum += A[j]
        if pSum not in aSub:
            aSub[pSum] = 1
        else:
            aSub[pSum] += 1

bSub = dict()
for i in range(m):
    pSum = 0
    for j in range(i, m):
        pSum += B[j]
        if pSum not in bSub:
            bSub[pSum] = 1
        else:
            bSub[pSum] += 1

bSums = sorted(bSub.keys())

for a in aSub.keys():
    
    target = T - a

    bi = bisect.bisect_left(bSums, target)

    if bi < len(bSums):
        if bSums[bi] == target:
            answer += bSub[bSums[bi]] * aSub[a]
        

print(answer)