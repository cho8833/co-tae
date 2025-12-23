A, B = map(int, input().split())

# 1 ~ 2**(n-1) 까지의 누적합
# f(n) = 2^(n-1) + 2 * f(n-1)
def prefixSum(n):
    if n == 1:
        return 1
    else:
        return 2**(n-1) + 2 * prefixSum(n-1)

def calcPS(target):
    if target == 0:
        return 0
    elif target == 1:
        return 1
    # 1. target 에 제일 가까운 2^n 찾기
    i = 1
    while 2 ** i <= target:
        i += 1
    i -= 1

    return prefixSum(i) + (target - 2**i + 1) + calcPS(target-2**i)

# 1~B 까지의 누적합 - 1~(A-1) 까지의 누적합
print(calcPS(B) - calcPS(A-1))