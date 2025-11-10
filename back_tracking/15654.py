N, M = map(int, input().split())

nums = list(map(int,input().split()))
nums.sort()

def recur(ns, prev, count):
    if count == 1:
        for i in range(len(ns)):
            print(prev + str(ns[i]))
        return
    for i in range(len(ns)):
        temp = ns[:]
        n = temp.pop(i)
        recur(temp, prev + str(n) + " ", count-1)

recur(nums, "", M)