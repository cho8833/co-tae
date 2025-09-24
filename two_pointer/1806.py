n, s = map(int, input().split())

nums = list(map(int, input().split()))

answer = 100000

left, right = 0,0

check = nums[0]

while True:
    if check < s:  # 합이 target 보다 작은 경우
        right += 1
        if right == n:
            break
        check += nums[right]
    else: # 합이 target 보다 큰 경우 - found
        length = right - left + 1
        answer = min(answer, length)
        if right == left and right < n:     # 길이가 1인 경우 바로 return
            answer = 1
            break
        else:
            check -= nums[left]
            left += 1

if answer == 100000:
    print(0)
else:
    print(answer)