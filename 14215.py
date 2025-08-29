n = list(map(int, input().split()))

maxLen = max(n)
n.remove(maxLen)
if maxLen >= n[0] + n[1]:
    print(n[0] * 2 + n[1] * 2 - 1)
else:
    print(maxLen + n[0] + n[1])
