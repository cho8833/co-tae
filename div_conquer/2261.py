import sys
m = int(input())

data = []
for _ in range(m):
    data.append(list(map(int, sys.stdin.readline().split())))

def dist(c1, c2):
    return (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2

data.sort(key= lambda x:x[0])

def div_conquer(start, end):
    global data

    n = end - start

    if n <= 3:
        minDist = float('inf')
        for i in range(start, end-1):
            for j in range(i + 1, end):
                minDist = min(minDist, dist(data[i], data[j]))
        return minDist


    mid = (start + end) // 2

    left = div_conquer(start, mid)
    right = div_conquer(mid, end)

    d = min(left, right)

    # 중간 지점 탐색
    midPoint = data[mid]

    temp = [midPoint]

        # 오른쪽 탐색
    for i in range(mid+1, end):
        if (data[i][0] - midPoint[0]) ** 2 < d:
            temp.append(data[i])
        else:
            break
        
        # 왼족 탐색
    for i in range(mid-1,start-1, -1):
        if (data[i][0] - midPoint[0]) ** 2 < d:
            temp.append(data[i])
        else:
            break

    temp.sort(key=lambda x:x[1])

    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            if (temp[i][1] - temp[j][1]) ** 2 < d:
                d = min(dist(temp[i], temp[j]), d)
            else:
                break
    return d

print(div_conquer(0, m))