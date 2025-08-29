n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

result1 = 0


def cal(v):
    r = v // t
    if v % t != 0:
        r += 1
    return r

for size in sizes:
    result1 += cal(size)

print(result1)
print(n // p, n % p)
