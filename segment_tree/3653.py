for _ in range(int(input())):
    N, m = map(int, input().split())

    MAX = N + m
    seg = [0] * (4 * MAX)

    height = [i for i in range(N-1, -1, -1)]

    maxHeight = N+1

    def init(start, end, i):
        if start == end:
            if start < N:
                seg[i] = 1
        else:
            mid = (start + end) // 2
            seg[i] = init(start, mid, i*2) + init(mid+1, end, i*2+1)
        return seg[i]
    
    def update(start, end, i, target, val):
        if target < start or target > end:
            return
        seg[i] += val
        if start == end:
            return
        mid = (start + end) // 2
        update(start, mid, i*2, target, val)
        update(mid+1, end, i*2+1, target, val)
    
    def segSum(start, end, i, left, right):
        if right < start or left > end:
            return 0
        if left <= start and right >= end:
            return seg[i]
        mid = (start + end) // 2
        return segSum(start, mid, i*2, left, right) + segSum(mid+1, end, i*2+1, left, right)
    

    init(0, MAX-1, 1)

    M = list(map(int, input().split()))
    for i in range(m):
        dvd = M[i] - 1

        targetHeight= height[dvd]

        # 출력
        print(segSum(0, MAX-1, 1, targetHeight+1, MAX-1), end=" ")

        # 빼기
        update(0, MAX-1, 1, targetHeight, -1)

        # 위에 놓기
        height[dvd] = maxHeight
        update(0, MAX-1, 1, maxHeight, 1)

        maxHeight += 1

    print() # 줄바꿈