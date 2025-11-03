N, M = map(int, input().split())

temp = list(map(int, input().split()))
known = None
if temp[0] == 0:
    known = []
else:
    known = temp[1:]

parent = [i for i in range(N+1)]

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parties = []
for _ in range(M):
    parties.append(list(map(int, input().split()))[1:])

if len(known) == 0:
    print(M)
    exit()

for k in range(len(known)):
    union(0, known[k])

# union
for party in parties:
    for n in range(1, len(party)):
        union(party[0], party[n])

        

answer = 0
for party in parties:
    isAnswer = True
    for n in party:
        if find(n) == 0:
            isAnswer = False
            break
    if isAnswer:
        answer += 1
print(answer)

