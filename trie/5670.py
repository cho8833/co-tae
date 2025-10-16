import sys


while True:
    try:
        n = int(input())
        words = []
        trie = dict()
        for _ in range(n):
            word = sys.stdin.readline().rstrip()
            chars = list(word)
            words.append(chars)
            if chars[0] not in trie:
                trie[chars[0]] = [0, False, dict()]
            
            temp = trie[chars[0]]
            for i in range(1, len(chars)):
                char = chars[i]
                if char not in temp[2]:
                    temp[2][char] = [0, False, dict()]
                temp[2][char][0] += 1
                temp = temp[2][char]
            temp[1] = True

        total = 0
        for word in words:
            temp = trie[word[0]]
            count = 1
            i = 1

            while i < len(word):
                if temp[0] == 1:
                    break
                if not len(temp[2].keys()) == 1 or temp[1]:
                    count += 1
                temp = temp[2][word[i]]
                i += 1

            total += count

        print("{0:.2f}".format(total / len(words)))
    except EOFError:
        break