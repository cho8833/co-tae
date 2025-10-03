import sys

stack = []
for _ in range(int(input())):
    cmd = list(map(int, sys.stdin.readline().rstrip().split()))

    if len(cmd) == 1:
        if cmd[0] == 4:
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif cmd[0] == 3:
            print(len(stack))
        elif cmd[0] == 2:
            if len(stack) > 0:
                print(stack.pop())
            else:
                print(-1)
        elif cmd[0] == 5:
            if len(stack) > 0:
                print(stack[-1])
            else:
                print(-1)

    else:
        if cmd[0] == 1:
            stack.append(cmd[1])