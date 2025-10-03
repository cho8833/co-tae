n = int(input())

local = list(map(int, input().split()))

m = int(input())

local.sort()

def check(x):
    global local
    global m
    temp = 0
    i = 0
    while True:
        if local[i] < x:
            temp += local[i]
        else:
            break
        i+= 1
    temp += x * (len(local) - i)

    if temp <= m:
        return True
    else:
        return False


if check(local[-1]):  # 모든 요청이 배정될 수 있는 경우
    print(local[-1])
else:
    left, right = 0, local[-1]

    while left + 1 < right:
        mid = (left + right) // 2
        
        if check(mid):
            left = mid
        else:
            right = mid
    print(left)