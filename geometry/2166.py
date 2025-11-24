N = int(input())

points = []

rx, ry = map(int, input().split())
points.append((rx, ry))
for _ in range(N-1):
    x, y = map(int, input().split())
    points.append((x, y))
points.append((rx, ry))

p1 = 0
p2 = 0
for i in range(0, N):
    p1 += points[i][0] * points[i+1][1]
    p2 += points[i][1] * points[i+1][0]
    
    

print(round(abs(p1-p2) / 2, 1))