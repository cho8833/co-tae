exp = input()

stack = []

answer = ""

def priority(symbol):
    if symbol == "(" or symbol == ")":
        return 0
    elif symbol == "+" or symbol == "-":
        return 1
    elif symbol == "*" or symbol == "/":
        return 2
    

for i in range(len(exp)):
    symbol = exp[i]

    if symbol.isalpha():
        answer += symbol
    elif symbol == "+" or symbol == "-" or symbol == "*" or symbol == "/":
        while stack:
            if priority(symbol) <= priority(stack[-1]):
                answer += stack.pop()
            else:
                break
        stack.append(symbol)
    elif symbol == "(":
        stack.append(symbol)
    elif symbol == ")":
        while stack:
            s = stack.pop()
            if s == "(":
                break
            answer += s

while stack:
    answer += stack.pop()

print(answer)