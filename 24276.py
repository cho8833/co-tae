n = int(input())
result = 0
for i in range(n-2):
    print(i)
    for j in range(i+1, n-1):
        print("\t",j)
        for k in range(j+1, n):
            print("\t\t", k)
            result += 1
print(result)
