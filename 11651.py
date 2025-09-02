import sys

data = []
for _ in range(200001):
    data.append([])
for _ in range(int(sys.stdin.readline())):
    n1, n2 = map(int,sys.stdin.readline().split(' '))
    data[n2].append(n1)

for i in range(-100000, 100001, 1):
    if len(data[i]) != 0:
        d = sorted(data[i])

        for o in d:
            print(o,i)
