n = int(input())

nums = list(map(int, input().split()))

x = int(input())

nums.sort()

answer = 0

left, right = 0, len(nums) -1

while left < right:
    check = nums[left] + nums[right]

    if check > x:
        right -= 1
    elif check < x:
        left += 1
    else:
        answer += 1
        left += 1
        right -= 1
print(answer)