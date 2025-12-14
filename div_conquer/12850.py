D = int(input())

mat = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]

def mult(m1, m2):
    result = []
    for i in range(8):
        row = []
        for j in range(8):
            temp = 0
            for k in range(8):
                temp += (m1[i][k] * m2[k][j])
            row.append(temp % 1_000_000_007)
        result.append(row)
    return result

def divConquer(count):
    if count == 1:
        return mat
    d = divConquer(count // 2)
    if count % 2 == 0:
        return mult(d, d)
    else:
        return mult(mult(d, d), mat)

result = divConquer(D)
print(result[0][0])
