code = list(map(int, list(input())))
if code[0] == 0:
    print(0)
    exit()
if len(code) == 1:
    print(1)
    exit()
dp = [0] * len(code)

MOD = 1_000_000
dp[0] = 1
dp[1] = 0

if code[1] != 0:
    dp[1] += 1
else:
    if dp[0] > 2:
        print(0)
        exit()
if code[0] * 10 + code[1] < 27:
    dp[1] += 1

for i in range(2, len(code)):
    if code[i] != 0:
        dp[i] += dp[i-1]
    else:
        if code[i-1] > 2:
            print(0)
            exit()
    if code[i-1] * 10 + code[i] < 27 and code[i-1] != 0:
        dp[i] += dp[i-2]
    dp[i] %= MOD
print(dp[-1])