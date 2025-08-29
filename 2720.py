coin = [25, 10, 5, 1]
for _ in range(int(input())):
    result = [0] * 4
    n = int(input())
    temp = n
    for i in range(len(coin)-1):
        value, rest = divmod(temp, coin[i])
        result[i] = value
        temp = rest
        if rest == 0:
            break
    result[3] = temp
    print(*result)
