s = list(map(int, input().split()))
n = s[0]
result = []
temp = s[0]
nd = 1
while True:
    if temp < 1:
        break
    if n % temp == 0:
        result.append(temp)
    temp -= 1

if len(result) < s[1]:
    print("0")
else:
    print(result[-s[1]])
