cmd = list(map(int, input().split()))

length = 0

for i in range(len(cmd)):
    if cmd[i] == 0:
        break
    length += 1


# dp[cmd][r][c]
dp = [[[float('inf')] * 5 for _ in range(5)] for _ in range(length)]

dp[0][0][cmd[0]] = 2
dp[0][cmd[0]][0] = 2

for i in range(1, length):
    c = cmd[i]

    for r in range(5):
        for l in range(5):
            if dp[i-1][r][l] != float('inf'):
                # 오른쪽 움직이기
                force = 0
                if r == 0:
                    force = 2
                elif r == c:           # 같은 판
                    force = 1
                elif abs(r-c) == 2:  # 반대편
                    force = 4
                else:
                    force = 3
                dp[i][c][l] = min(dp[i][c][l], dp[i-1][r][l] + force)
                
                # 왼쪽 움직이기
                if l == 0:
                    force = 2
                elif l == c:          # 같은 판
                    force = 1
                elif abs(l - c) == 2:
                    force = 4
                else:
                    force = 3
                dp[i][r][c] = min(dp[i][r][c], dp[i-1][r][l] + force)

print(min(map(min, dp[length-1])))