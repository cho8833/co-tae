import bisect

N = int(input())

L = list(map(int, input().split()))

L.sort()

answer = float('inf')
a1, a2, a3 = 0, 0, 0

for i in range(N-2):
    for j in range(i+1, N-1):
        l2 = L[i] + L[j]
        k = bisect.bisect_left(L, -l2, lo=j+1)
        if k < N:
            t = abs(l2 + L[k])
            if answer > t:
                answer = t
                a1, a2, a3 = L[i], L[j], L[k]
        if j+1 < k < N+1:
            t = abs(l2 + L[k-1])
            if answer > t:
                answer = t
                a1, a2, a3 = L[i], L[j], L[k-1]
        

print(a1, a2, a3)