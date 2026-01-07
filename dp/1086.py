N = int(input())

data = [int(input()) for _ in range(N)]

K = int(input())

dp = [[0] * (K) for _ in range(1 << N)]

dataMod = [0] * N

for i in range(N):
    dataMod[i] = data[i] % K

dp10Mod = [-1] * 751
dp10Mod[1] = 10 % K

dataLength = [len(str(data[i])) for i in range(N)]

length = [[0] * K for _ in range(1 << N)]

def calc10Mod(i):
    if dp10Mod[i] == -1:
        dp10Mod[i-1] = calc10Mod(i-1)
        return (dp10Mod[1] * dp10Mod[i-1]) % K
    else:
        return dp10Mod[i]


# init
for i in range(N):
    m = data[i] % K
    dp[1<<i][m] = 1
    length[1<<i][m] = dataLength[i]

for state in range(1 << N):
    for mod in range(K):
        if dp[state][mod] > 0:
            len_ = length[state][mod]
            
            for n in range(N):
                if state & 1 << n == 0:
                    m = (mod + (calc10Mod(len_) * dataMod[n]) % K) % K
                    dp[state | 1 << n][m] += dp[state][mod]
                    length[state | 1 << n][m] = len_ + dataLength[n]

def factorial(i):
    if i == 1:
        return 1
    else:
        return factorial(i-1) * i

p = dp[(1 << N) - 1][0]
q = factorial(N)

p_, q_ = p, q

while q_ != 0:
    p_, q_ = q_, p_%q_

print(str(p // p_) + "/" + str(q // p_))