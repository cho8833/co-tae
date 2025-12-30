import sys
input = sys.stdin.readline

N = int(input())

parent = list(range(N))

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
        return parent[a]
    return a


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def ccw(p1, p2, p3):
    s = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    if s > 0:
        return 1
    elif s < 0:
        return -1
    else:
        return 0
    
def isIntersect(p1, p2, p3, p4):
    ccw1 = ccw(p1,p2,p3) * ccw(p1,p2,p4)
    ccw2 = ccw(p3,p4,p1) * ccw(p3,p4,p2)

    if ccw1 <= 0 and ccw2 <= 0:
        if ccw1 == 0 and ccw2 == 0:
            
            return min(p1[0], p2[0]) <= max(p3[0], p4[0]) and min(p3[0], p4[0]) <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= max(p3[1], p4[1]) and min(p3[1], p4[1]) <= max(p1[1], p2[1])
        else:
            return True
    else:
        return False
    
lines = []
for i in range(N):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    
    lines.append(((x1,y1), (x2,y2)))

for i in range(N):
    for j in range(i+1, N):
        if isIntersect(lines[i][0], lines[i][1], lines[j][0], lines[j][1]):
            union(i, j)

maxAnswer = 1

answer = dict()
for i in range(len(parent)):
    p = find(i)
    if p in answer:
        answer[p] += 1
        maxAnswer = max(maxAnswer, answer[p])
    else:
        answer[p] = 1
        
    
print(len(answer.keys()))
print(maxAnswer)