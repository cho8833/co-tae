N, M = map(int, input().split())
data = list(map(int, input().split()))

data = list(set(data))
data.sort()

length = len(data)

seq = []

def recur(i, n):
    if n == M:
        print(" ".join(map(str, seq)))
        return
    for j in range(i, length):
        seq.append(data[j])
        recur(j, n+1)
        seq.pop()
recur(0, 0)