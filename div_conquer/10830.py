import bisect

n, b = map(int, input().split())

mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

data = {}
def mult(mat):
    global n
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        row = mat[i]
        for j in range(n):
            temp = 0
            for k in range(n):
                temp += (row[k] * mat[k][j])
            result[i][j] = temp % 1000
    return result

