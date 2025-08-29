s = list(map(int, input().split(' ')))

basket = list(range(1, s[0] + 1, 1))

for _ in range(s[1]):
    s = list(map(lambda x:int(x) -1, input().split(' ')))
    basket[s[0]:s[1]+1] = reversed(basket[s[0]: s[1]+1])

print(*basket)
