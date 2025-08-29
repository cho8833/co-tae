s = input()

sp = s.split(' ')

sp = list(map(int, sp))

basket = list(range(1, sp[0]+ 1, 1))

for i in range(sp[1]):
    s = input()
    sp = list(map(int, s.split(' ')))
    sp = list(map(lambda x:x - 1, sp))
    temp = basket[sp[0]]
    basket[sp[0]] = basket[sp[1]]
    basket[sp[1]] = temp

print(*basket, sep=' ')
    
