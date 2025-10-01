n = int(input())

dp = [0] * (n+1)
dp[1] = 1

nums = []
i = 2
while True:
    t = i ** 2
    if t <= n:
        nums.append(t)
    else:
        break
    i += 1

        
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    for j in range(len(nums)):
        if nums[j] <= i:
            dp[i] = min(dp[i-nums[j]]+1, dp[i])
        else:
            break

print(dp[n])