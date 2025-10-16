n = int(input())

solution = list(map(int, input().split()))

test = 2000000000
answer = []
left = 0
right = n - 1

while left < right:
    temp = solution[left] + solution[right]
    if abs(temp) <= test:
        answer = [solution[left], solution[right]]
        test = abs(temp)
    if temp >= 0:
        right -= 1
    else:
        left += 1

print(answer[0], answer[1])