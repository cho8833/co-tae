N, B = map(int, input().split())

mat = []
for _ in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        row[j] = row[j] % 1000
    mat.append(row)

dp = dict()

dp[1] = mat

def mult(mat1, mat2):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp = 0
            for k in range(N):
                temp += mat1[i][k] * mat2[k][j]
            result[i][j] = temp % 1000
    return result

def div_conquer(n):
    if n not in dp:
        k = n // 2
        if k not in dp:
            dp[k] = div_conquer(k)
        
        if n % 2 == 0:
            dp[n] = mult(dp[k], dp[k])
        else:
            dp[n] = mult(mat, mult(dp[k], dp[k]))

    return dp[n]

result = div_conquer(B)

for i in range(N):
    print(" ".join(map(str, result[i])))