n = int(input())

nums = list(map(int, input().split()))

minValue = 2000000000

answer = [0,0]

nums.sort()

# 배열의 양쪽 끝이 음수인 경우, 음수값 밖에 없음
if nums[0] < 0 and nums[n-1] < 0:
    print(nums[n-2], nums[n-1])
    exit()

# 배열의 양쪽 끝이 양수인 경우, 양수값 밖에 없음
elif nums[0] > 0 and nums[n-1] > 0:
    print(nums[0], nums[1])
    exit()
# 음수 양수가 섞인 경우
else:
    left, right = 0, len(nums) - 1
    while left < right:
        check = abs(nums[left] + nums[right])
        if check == 0:
            print(nums[left], nums[right])
            exit()
        
        if minValue > check:
            minValue = check
            answer = [nums[left], nums[right]]
        
        if abs(nums[left]) <= abs(nums[right]):
            right -= 1
        else:
            left += 1

print(answer[0], answer[1])