while True:
    n = int(input())
    if n == -1:
        break
    result = []
    temp = n-1
    while True:
        if temp < 1:
            break
        if n % temp == 0:
            result.append(temp)
        temp -= 1

    check = 0
    for i in result:
        check += i
    if check == n:
        print(n, "=", end=' ')
        print(*reversed(result), sep=' + ')
    else:
        print(n, "is NOT perfect.")
