while True:
    s = list(map(int, input().split()))
    if s[0] == 0 and s[1] == 0:
        break
    if s[0] < s[1]:
        if s[1] % s[0] == 0:
            print("factor")
            continue
    else:
        if s[0] % s[1] == 0:
            print("multiple")
            continue
    print("neither")
