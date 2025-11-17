N, M = map(int, input().split())

nums = list(map(int,input().split()))

answer = []

def recur(ns, prev, count):
    global answer
    if count == 1:
        for i in range(len(ns)):
            answer.append(prev + (ns[i], ))
        return
    for i in range(len(ns)):
        temp = ns[:]
        n = temp.pop(i)
        recur(temp, prev + (ns[i], ), count-1)

recur(nums, (), M)

answer = sorted(set(answer))

for a in answer:
    print(" ".join(map(str, a)))