for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    opt = max(x, y)
    temp = x
    x = y
    y = temp
    
    # 최대공약수 찾기
    gcd = x % y
    while True:
        y = y % gcd
        if temp == 0:
            break
        else:
            gcd = temp

    # 최소공배수 찾기
    lcm = m * n / gcd

    # 해 찾기
    while True:
        gcd = 
