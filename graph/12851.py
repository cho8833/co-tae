from collections import deque

N, K = map(int, input().split())

options = 0

queue = deque()

queue.append((N, 0))

time = [float('inf')] * 100_001

while queue:
    n, d = queue.popleft()

    if d > time[n]:
        continue
    if d > time[K]:
        break
    
    if n == K:
        if d < time[n]:
            time[n] = d
            options = 1
        elif d == time[n]:
            options += 1
        continue
    
    time[n] = d
    
    if n > 0:
        queue.append((n-1, d + 1))
    
    if n < 100_000:
        queue.append((n+1, d + 1))

    n2 = n * 2
    if n2 <= 100_000:
        queue.append((n2, d + 1))

print(time[K])
print(options)
