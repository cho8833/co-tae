import sys

n = int(input())

trie = dict()

for _ in range(n):
    split = sys.stdin.readline().rstrip().split()
    k = int(split[0])
    temp = trie
    for s in range(1, k+1):
        info = split[s]
        if info not in temp:
            temp[info] = dict()
        temp = temp[info]

def dfs(trie, depth):
    for key in sorted(trie.keys()):
        print("--" * depth + key)
        dfs(trie[key], depth+1)

dfs(trie, 0)