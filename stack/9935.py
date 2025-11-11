string = input()

ex = input()

i = 0

stack = []

while i < len(string):
    char = string[i]

    if char != ex[-1]:
        stack.append(char)
    else:
        if len(stack) >= len(ex)-1:
            isMatch = True
            for j in range(1, len(ex)):
                if stack[-j] != ex[-j-1]:
                    isMatch = False
                    break
            if isMatch:
                for _ in range(len(ex) - 1):
                    stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)
    i += 1


if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))