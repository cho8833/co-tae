import sys

def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

density = [0] * 30
n = int(sys.stdin.readline())
th = round2(n * 0.15)
for _ in range(n):
    h = int(sys.stdin.readline())
    density[h-1] += 1

high_th = th
low_th = th

for i in range(len(density)-1, -1, -1):
    if density[i] != 0:
        if density[i] >= high_th:
            density[i] -= high_th
            break
        else:
            high_th -= density[i]
            density[i] = 0

for i in range(0, len(density), 1):
    if density[i] != 0:
        if density[i] >= low_th:
            density[i] -= low_th
            break
        else:
            low_th -= density[i]
            density[i] = 0

result = 0

for i in range(len(density)):
    result += (i+1) * density[i]

if n != 0:
    print(round2(result / (n-(th * 2))))
else:
    print(0)