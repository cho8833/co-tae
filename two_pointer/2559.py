n, k = map(int, input().split())

nums = list(map(int, input().split()))

# 첫번째 윈도우
check = 0
for i in range(k):
    check += nums[i]
answer = check

for i in range(1, n-k+1):
    check -= nums[i-1]
    check += nums[i+k-1]
    answer = max(check, answer)
print(answer)