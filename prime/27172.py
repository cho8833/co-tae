N = int(input())

cards = list(map(int, input().split()))

order = dict()

for i in range(N):
    order[cards[i]] = i

cards.sort(reverse=True)

maxV = cards[0]

prime = [0] * (1_000_001)

for i in range(1, N):
    
    card = cards[i]
    j = 2

    temp = card * j

    while temp < maxV+1:
        if temp in order:
            prime[card] += 1
        prime[temp] -= 1

        j += 1
        temp = card * j

answer = [0] * N
for card, i in order.items():
    answer[i] = prime[card]

print(*answer)