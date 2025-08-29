while True:
    n = list(map(int, input().split()))
    if n[0] == 0 and n[1] == 0 and n[2] == 0:
        break
    maxLen = max(n)
    n.remove(maxLen)
    if maxLen >= n[0] + n[1]:
        print("Invalid")
    else:
        if maxLen == n[0] and maxLen == n[1] and n[0] == n[1]:
            print("Equilateral")
        elif maxLen == n[0] or maxLen == n[1] or n[0] == n[1]:
            print("Isosceles")
        else:
            print("Scalene")
