import sys
import bisect
sys.setrecursionlimit(10000**2)
data = []

while True:
    try:
        data.append(int(sys.stdin.readline()))
    except:
        break

def postorder(left, right):
    global data
    if left >= right:
        return
    root = data[left]

    idx = bisect.bisect_left(data, root, lo=left+1, hi=right)
    postorder(left+1, idx)
    postorder(idx, right)

    print(root)

postorder(0, len(data))


