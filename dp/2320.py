dictionary = {
    "A": 0,
    "E": 1,
    "I": 2,
    "O": 3,
    "U": 4,
}

N = int(input())

# word = [first word, last word, length]
words = []

for _ in range(N):
    word = input()
    words.append((dictionary[word[0]], dictionary[word[-1]], len(word)))

# dp[bit][lastword] = length
dp = [[0] * 5 for _ in range(1 << N)]

# init
for n in range(N):
    dp[1 << n][words[n][1]] = words[n][2]

answer = 0
for state in range(1 << N):
    for lastWord in range(5):
        if dp[state][lastWord] > 0:
            length = dp[state][lastWord]
            answer = max(answer, length)
            for n in range(N):
                if state & 1 << n == 0 and lastWord == words[n][0]:
                    nextState = state |  1 << n
                    dp[nextState][words[n][1]] = max(dp[nextState][words[n][1]], length + words[n][2])

print(answer)