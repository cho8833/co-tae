N = int(input())

MOD = 1_000_000_007

mat = [
    [4, -1],
    [1, 0]
]

def mult(m1, m2):
    result = [
        [0, 0],
        [0, 0]
    ]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += (m1[i][k] * m2[k][j])
            if result[i][j] > 0:
                result[i][j] %= MOD
            else:
                result[i][j] %= -MOD
    return result

def div(n):
    if n in dp:
        return dp[n]
    if n == 1:
        return mat
    if n % 2 == 0:
        dp[n] = mult(div(n//2), div(n//2))
    else:
        dp[n] = mult(mult(div(n//2), div(n//2)), mat)
    return dp[n]
    
    
dp = dict()

if N == 1:
    print(3)
elif N % 2 == 1:
    print(0)
else:
    result = div(N // 2)
    print((result[1][0] * 3 + result[1][1]) % MOD)