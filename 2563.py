n = []
for _ in range(100):
    n.append([True]*100)
area = 0
for _ in range(int(input())):
    s = list(map(lambda x:int(x)-1, input().split()))
    for i in range(s[0], s[0]+10, 1):
        for j in range(s[1], s[1]+10, 1):
            if n[i][j]:
                n[i][j] = False
                area += 1
print(area)
