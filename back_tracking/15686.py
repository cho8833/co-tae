N, M = map(int, input().split())
chickenLocation = []
houseLocation = []
for i in range(N):
    row = [-1]
    row.extend(list(map(int, input().split())))
    for j in range(1, len(row)):
        if row[j] == 2:
            chickenLocation.append((i+1, j))
        elif row[j] == 1:
            houseLocation.append((i+1, j))

totalClose = len(chickenLocation) - M

answer = 1e9

include = [True] * len(chickenLocation)

def calc(house):
    result = 1e9
    for i in range(len(chickenLocation)):
        if include[i]:
            chicken = chickenLocation[i]
            result = min(result, abs(chicken[0] - house[0]) + abs(chicken[1] - house[1]))
    return result

    
def recur(c, close):
    global answer
    if close == totalClose:
        chickenDist = 0
        # calc chicken distance
        for house in houseLocation:
            chickenDist += calc(house)
        answer = min(chickenDist, answer)    
        return

    
    for i in range(c, len(include)):
        include[i] = False
        recur(i+1, close+1)
        include[i] = True

recur(0, 0)
print(answer)