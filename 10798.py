s = []
max_len = 0
for _ in range(5):
    temp = list(input())
    if max_len < len(temp):
        max_len = len(temp)
    s.append(temp)
r = []
for i in range(5):
    temp = [''] * max_len
    temp[:len(s[i])] = s[i]
    r.append(temp)

for j in range(max_len):
    for i in range(5):
        print(r[i][j], end="")
