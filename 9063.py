max_p = []

min_p = []

for i in range(int(input())):
    s = list(map(int, input().split()))
    if i == 0:
        max_p = s[:]
        min_p = s[:]
        continue
    
    if s[0] > max_p[0]:
        max_p[0] = s[0]
    elif s[0] < min_p[0]:
        min_p[0] = s[0]

    if s[1] > max_p[1]:
        max_p[1] = s[1]
    elif s[1] < min_p[1]:
        min_p[1] = s[1]

print((max_p[0] - min_p[0]) * (max_p[1] - min_p[1]))
