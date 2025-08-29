n = [0] * 30

for _ in range(28):
    s = int(input())
    n[s-1] = 1

result = []
for i in range(len(n)):
    if n[i] == 0:
        result.append(i+1)

print(*result, sep='\n')
