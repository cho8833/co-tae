class Node:
    def __init__(self, value, isTarget):
        self.value = value
        self.isTarget = isTarget

result = 1
target = 0

def search(queue):
    global result
    v = queue[0]
    for i in range(1, len(queue)):
        if v.value < queue[i].value:
            queue.append(queue.pop(0))
            search(queue)
            return
    if v.isTarget:
        print(result)
        return
    queue.pop(0)
    result += 1
    search(queue)


for _ in range(int(input())):
    length, targetIndex = map(int, input().split())
    queue = list(map(lambda x: Node(x, False), input().split()))
    queue[targetIndex].isTarget = True
    result = 1
    search(queue)
