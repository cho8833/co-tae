import sys

M = int(input())

m = 1_000_000_007

answer = 0

dices = []
    

for _ in range(M):
    N, S = map(int, sys.stdin.readline().rstrip().split())
    S = S % m

    dp = dict()
    dp[1] = N % m

    def dc(n):
        if n not in dp:
            # 짝수일 때
            if n % 2 == 0:
                dp[n] = (dc(n//2) ** 2) % m

            # 홀수일 때
            else:
                dp[n] = ((dc(n//2)**2) * dp[1]) % m
            
        return dp[n]
    
    answer = (answer + ((S * dc(m-2)) % m)) % m

print(answer)