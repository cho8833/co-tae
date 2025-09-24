n, m = map(int, input().split())

nums = list(map(int, input().split()))

left, right = 0, 0

answer = 0

check = nums[0]
while True:
    
    if check < m:       # 합이 목표보다 작은 경우
        right += 1
        if right == n:
            break
        check += nums[right]
    elif check > m:     # 합이 목표보다 큰 경우
        if left == right and right < n-1:
            left += 1
            right += 1
            check = nums[left]
        check -= nums[left]
        left += 1
    else:               # 찾은 경우
        answer += 1
        right += 1
        if right == n:
            break
        check += nums[right]
        check -= nums[left]
        left += 1

print(answer)
