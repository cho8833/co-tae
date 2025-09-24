# find prime
n = int(input())
if n == 1:
    print(0)
    exit()

filter = [True for _ in range(n+1)]
filter[0] = False
filter[1] = False
for i in range(2, n//2+1):
    if filter[i]:
        for j in range(i*i, n+1, i):
            filter[j] = False

primes = []
for i in range(len(filter)):
    if filter[i]:
        primes.append(i)
left, right = 0, 0

answer = 0
check = primes[0]
while True:
    if check < n:
        right += 1
        if right == len(primes):
            break
        check += primes[right]

    elif check > n:
        if right == left and right < n - 1:
            right += 1
            left += 1
            check = primes[right]
        else:
            check -= primes[left]
            left += 1
    
    else:
        answer += 1
        right += 1
        if right == len(primes):
            break
        check += primes[right]

        check -= primes[left]
        left += 1
print(answer)