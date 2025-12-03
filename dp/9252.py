s1 = input()
s2 = input()

dp = [[None] * len(s1) for _ in range(len(s2))]

dp[0][0] = 1 if s1[0] == s2[0] else 0
for i in range(1, len(s1)):
    if s1[i] == s2[0]:
        dp[0][i] = 1
    else:
        dp[0][i] = dp[0][i-1]

for j in range(1, len(s2)):
    if s1[0] == s2[j]:
        dp[j][0] = 1
    else:
        dp[j][0] = dp[j-1][0]

for i in range(1, len(dp)):
    for j in range(1, len(dp[i])):
        if s1[j] == s2[i]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

lAnswer = dp[len(s2)-1][len(s1)-1]
if lAnswer == 0:
    print(0)
    exit()
    
answer = []
i = len(s2)-1
j = len(s1)-1

while True:
    if s1[j] == s2[i]:
        answer.append(s1[j])
        if dp[i][j] == 1:
            break
        else:
            i = max(i-1, 0)
            j = max(j-1, 0)
            continue
    
    if dp[i][j-1] == dp[i][j]:
        if j > 0:
            j -= 1
        else:
            i -= 1
    else:
        if i > 0:
            i -= 1
        else:
            j -= 1
    
print(dp[len(s2)-1][len(s1)-1])
for i in range(len(answer)-1,-1,-1):
    print(answer[i], end='')