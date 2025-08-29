s = list(map(int, input().split(' ')))

s1 = []

for _ in range(s[0]):
    s1.append(list(map(int,input().split(' '))))

s2 = []
for _ in range(s[0]):
    s2.append(list(map(int, input().split(' '))))

for i in range(s[0]):
    temp = []
    for j in range(s[1]):
        temp.append(s1[i][j] + s2[i][j])
    print(*temp)

