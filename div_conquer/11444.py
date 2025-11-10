N = int(input())

dp = dict()

def fibbo(n):
    global dp
    if n == 0:
        return 0
    elif n < 3:
        return 1
    else:
        if n % 2 == 0:
            k = n // 2

            if k not in dp:
                dp[k] = fibbo(k)
            fk = fibbo(k)

            if k-1 not in dp:
                dp[k-1] = fibbo(k-1)

            f_1k = dp[k-1]
            return (fk * (2 * f_1k + fk)) % 1_000_000_007
        else:
            k = n // 2
            if k not in dp:
                dp[k] = fibbo(k)
            
            if k+1 not in dp:
                dp[k+1] = fibbo(k+1)
            fk = dp[k]
            f_1k = dp[k+1]
            return (f_1k ** 2 + fk ** 2) % 1_000_000_007

print(fibbo(N))
