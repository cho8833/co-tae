x1, y1, x2, y2 = map(int, input().split())

p1 = (x1, y1)

p2 = (x2, y2)

x1, y1, x2, y2 = map(int, input().split())

p3 = (x1, y1)

p4 = (x2, y2)

def ccw(p1, p2, p3):
    result = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    if result > 0:
        return 1
    elif result < 0:
        return -1
    else:
        return 0

def isIntersect(p1, p2, p3, p4):
    ccw1 = ccw(p1,p2,p3) * ccw(p1,p2,p4)
    ccw2 = ccw(p3,p4,p1) * ccw(p3,p4,p2)

    if ccw1 <= 0 and ccw2 <= 0:
        if ccw1 == 0 and ccw2 == 0:
            # 일직선 상에 있을 때

            return min(p1[0], p2[0]) <= max(p3[0], p4[0]) and min(p3[0], p4[0]) <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= max(p3[1], p4[1]) and min(p3[1], p4[1]) <= max(p1[1], p2[1])
        else:
            return True
    else:
        return False

if isIntersect(p1, p2, p3, p4):
    print(1)
else:
    print(0)