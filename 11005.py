s = list(map(int, input().split()))

n = s[0]
f = s[1]
result = []
temp = n

while True:
    value, rest = divmod(temp, f)
    result.append(rest)
    if value == 0:
        break
    else:
        temp = value

for i in range(len(result)-1, -1, -1):
    r = result[i]
    if r > 9:
        print(chr(55+r), end='')
    else:
        print(r, end='')
