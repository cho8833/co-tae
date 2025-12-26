import sys
sys.setrecursionlimit(10**6)

N = int(input())

I = list(map(int, input().split()))
P = list(map(int, input().split()))

idx = [0] * (N+1)

for i in range(N):
    idx[I[i]] = i

def calc(il, ir, pl ,pr):
    if il > ir:
        return
    
    root = P[pr]

    print(root, end=' ')

    
    # find root in inorder
    rootIdx = idx[root]
    
    length = rootIdx - il

    # left
    calc(il, rootIdx-1, pl, pl+length-1)
    # right
    calc(rootIdx+1, ir, pl+length, pr-1)
    

calc(0, N-1, 0, N-1)