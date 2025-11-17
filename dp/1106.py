C, N = map(int, input().split())

city = []

for _ in range(N):
    c, p = map(int, input().split())
    city.append((c, p))

dp = [float('inf')] * (C+100)
dp[0] = 0

for i in range(1, len(dp)):
    # i : target people
    # dp[i] : cost of target people
    for cost, people in city:
        if i < people:
            continue
        dp[i] = min(dp[i], dp[i-people] + cost)
print(min(dp[C:]))