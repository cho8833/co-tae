s = []

for _ in range(9):
    s.append(list(map(int, input().split(' '))))

v = s[0][0]
row = 1
col = 1
for i in range(len(s)):
    for j in range(len(s[i])):
        if v < s[i][j]:
            v = s[i][j]
            col = i+1
            row = j+1

print(v)
print(col, row)
