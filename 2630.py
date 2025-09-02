n = int(input())
data = []
blue = 0
white = 0
def div(field):
    global blue, white
    check = field[0][0]
    middle = len(field) // 2
    for i in range(len(field)):
        for j in range(len(field[i])):
            if check != field[i][j]:
                f1 = [row[0:middle] for row in field[0:middle]]
                f2 = [row[middle:] for row in field[middle:]]
                f3 = [row[0:middle] for row in field[middle:]]
                f4 = [row[middle:] for row in field[0:middle]] 
                div(f1)
                div(f2)
                div(f3)
                div(f4)
                return
    if check == 0:
        white += 1
    else:
        blue += 1

for _ in range(n):
    data.append(list(map(int, input().split(' '))))

div(data)
print(white)
print(blue)
