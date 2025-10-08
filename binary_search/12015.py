n = int(input())
nums = list(map(int, input().split()))
m = [-float('inf'), nums[0]]

for i in range(1, n):

    num = nums[i]
    left, right = 0, len(m)

    if m[-1] < num:
        m.append(num)
        continue
    
    while left + 1 < right:
        
        mid =(left + right) // 2

        if m[mid] < num:
            left = mid
        else:
            right = mid
    
    m[right] = num
print(len(m) - 1)