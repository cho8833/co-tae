N, S, E, T = map(int, input().split())

mat = [[0] * (5 * N) for _ in range(5 * N)]

for r in range(N):
        for k in range(1, 5):
            mat[r * 5 + k][r * 5 + k - 1] = 1


for r in range(N):
    row = list(map(int, list(input())))
    for c in range(N):
        if row[c] == 0:
            continue
        else:
            mat[r * 5][c * 5 + row[c] - 1] = 1


def mult(m1, m2):
    result = []
    for r in range(N * 5):
        row = []
        for c in range(N * 5):
            temp = 0
            for i in range(N * 5):
                temp += m1[r][i] * m2[i][c]
            row.append(temp % 1_000_003)
        result.append(row)
    return result

def div_conquer(count):
    if count == 1:
        return mat
    d = div_conquer(count // 2)
    if count % 2 == 0:
        return mult(d, d)
    else:
        return mult(mult(d, d), mat)

result = div_conquer(T)
print(result[5 * (S-1)][5 * (E-1)])