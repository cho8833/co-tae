string = input()

length = len(string)

pal = [[None] * length for _ in range(length)]

for i in range(length):
    pal[i][i] = True
for i in range(length-1):
    if string[i] == string[i+1]:
        pal[i][i+1] = True
    else:
        pal[i][i+1] = False
dp = list(range(1, length + 2))
dp[-1] = 0


def isPal(i, j):
    if pal[i][j] != None:
        return pal[i][j]

    if i > j:
        return True
    if string[i] == string[j]:
        return isPal(i+1, j-1)
    else:
        return False

for i in range(length):
    for j in range(i+1):
        pal[j][i] = isPal(j, i)
        if pal[j][i]:
            dp[i] = min(dp[i], dp[j-1] + 1)

print(dp[-2])