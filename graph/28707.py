import heapq

N = int(input())

A = list(map(int, input().split()))

M = int(input())

ctrl = []

for _ in range(M):
    l, r, c = map(int, input().split())
    ctrl.append((l-1, r-1, c))

def cvt(node):
    result = 0

    for i in range(N):
        if node[i] == 10:
            continue
        result += node[i] * 10**(N-1-i)
    return result

data = dict()

a = cvt(A)
data[a] = A

visited = dict()
visited[a] = 0

hq = [(0, cvt(A))]

while hq:
    
    d, a = heapq.heappop(hq)

    # check
    A = data[a]
    temp = A[0]
    isComplete = True
    for i in range(1, N):
        if temp <= A[i]:
            temp = A[i]
        else:
            isComplete = False
            break
    if isComplete:
        print(d)
        exit()
    

    
    if d > visited[a]:
        continue
    
    for l, r, c in ctrl:
        node = data[a][:]
        node[l], node[r] = node[r], node[l]

        n = cvt(node)
        data[n] = node

        if n in visited:
            if visited[n] > visited[a] + c:
                visited[n] = visited[a] + c
                heapq.heappush(hq, (visited[n], n))
        else:
            visited[n] = visited[a] + c
            heapq.heappush(hq, (visited[a] + c, n))

print(-1)