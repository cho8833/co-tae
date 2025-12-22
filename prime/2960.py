N, K = map(int, input().split())

sieve = [True] * (N+1)

sieve[1] = False

for i in range(2, N+1):
    if sieve[i]:

        j = 1
        temp = i

        while temp < N+1:
            if sieve[temp]:
                sieve[temp] = False
                K -= 1
                if K == 0:
                    print(temp)
                    exit()

            j += 1
            temp = i * j

        