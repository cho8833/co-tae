from collections import deque
n = int(input())

data = list(map(int, input().split()))

answer = 0
order = deque()
fruits = {}
lastIndex = {}
for i in range(n):
    
    if data[i] not in fruits:
        if len(fruits.keys()) == 2:
            
            # 최대값 계산
            temp = 0
            for num in fruits.keys():
                temp += fruits[num]
            answer = max(answer, temp)

            # 삭제
            pop = order.popleft()
            del fruits[pop]

            fruits[order[0]] = lastIndex[order[0]] - lastIndex[pop]
        
        fruits[data[i]] = 1
        order.append(data[i])
    else:
        fruits[data[i]] += 1
        if order[-1] != data[i]:
            order.popleft()
            order.append(data[i])
    lastIndex[data[i]] = i

temp = 0
for num in fruits.keys():
    temp += fruits[num]
answer = max(answer, temp)

print(answer)


