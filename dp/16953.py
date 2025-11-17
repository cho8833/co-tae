from collections import deque

A, B = map(int, input().split())

dp = dict()

dp[A] = 1

q = deque([A])

while q:
    n = q.popleft()

    for i in n * 2, n *10 + 1:
        if i > B:
            continue
        if i not in dp:
            dp[i] = dp[n] + 1
            q.append(i)
        else:
            if dp[i] > dp[n] + 1:
                dp[i] = dp[n] + 1
                q.append(i)

if B not in dp:
    print(-1)
else:
    print(dp[B])