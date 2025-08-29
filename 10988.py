s = input()

length = len(s)
result = 1
for i in range(length//2):
    if s[i] != s[-i-1]:
        result = 0
        break
    
print(result)
