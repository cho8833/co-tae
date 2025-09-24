from collections import deque

n, k = map(int, input().split())

table = [float('inf') for _ in range(100001)]

queue = deque()

num = n
if num == 0:
    table[0] = 0
    table[1] = 1
    queue.append(0)
    queue.append(1)
else:
    while num <= 100000:
        table[num] = 0
        queue.append(num)
        if num == k:
            print(table[num])
            exit()
        num *= 2

while len(queue) != 0:
    num = queue.popleft()

    if num == k:
        print(table[num])
        exit()
    # num - 1
    minus = num-1
    if minus > 0:
        while minus <= 100000:
            dist = table[num] + 1
            if dist < table[minus]:
                table[minus] = dist
                queue.append(minus)
            minus *= 2
    elif minus == 0:
        if table[num] + 1 < table[0]:
            queue.append(0)
            table[0] = table[num] + 1

    # num + 1
    plus = num + 1
    if plus < 100001:
        while plus <= 100000:
            dist = table[num] + 1
            if dist < table[plus]:
                table[plus] = dist
                queue.append(plus)
            plus *= 2
    