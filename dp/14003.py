import bisect

N = int(input())

S = list(map(int, input().split()))

lis = [[(0,S[0])]]

for i in range(N):
    k = bisect.bisect_left(lis, S[i], key = lambda x:x[-1][1])
    if len(lis) == k:
        lis.append([(i, S[i])])
    else:
        lis[k].append((i, S[i]))

answer = [lis[-1][-1][1]]
lastIndex = lis[-1][-1][0]

for i in range(len(lis)-2, -1, -1):
    l = bisect.bisect_left(lis[i], lastIndex, key= lambda x:x[0])

    answer.append(lis[i][l-1][1])
    lastIndex = lis[i][l-1][0]
print(len(lis))
for i in range(len(answer)-1, -1, -1):
    print(answer[i], end=" ")