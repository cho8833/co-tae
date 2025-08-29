s = input().split()

n = list(s[0])

f = int(s[1])

result = 0
for i in range(len(n)-1, -1, -1):
    number = 0
    
    check = ord(n[i])
    if check > 64:
        number = check - 55
    else:
        number = int(n[i])

    result += number * (f ** (len(n) - i-1))

print(result)
