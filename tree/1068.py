n = int(input())

s = list(map(int, input().split()))

data = dict()

root = 0
for i in range(len(s)):
    if s[i] == -1:
        root = i
    else:
        if s[i] not in data:
            data[s[i]] = [i]
        else:
            data[s[i]].append(i)

delete = int(input())

answer = 0
def dfs(node):
    global answer
    if node == delete:
        return

    if node not in data:
        answer += 1
    else:
        children = data[node]
        if len(children) > 1:
            for child in children:
                if child != delete:
                    dfs(child)
        else:
            if children[0] == delete:
                answer += 1
                return
            else:
                dfs(children[0])

dfs(root)

print(answer)
    
        