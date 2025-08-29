s = input()

splited = s.split(' ')

basket = [0] * int(splited[0])

for i in range(int(splited[1])):
    s1 = input()
    sp = s1.split(' ')
    n = int(sp[2])
    for j in range(int(sp[0])-1, int(sp[1]), 1):
        
        basket[j] = n
        
print(*basket)
