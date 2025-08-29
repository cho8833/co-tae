p_x = []
p_y = []
for _ in range(3):
    temp = list(map(int, input().split()))
    if temp[0] in p_x:
        p_x.remove(temp[0])
    else:
        p_x.append(temp[0])
    if temp[1] in p_y:
        p_y.remove(temp[1])
    else:
        p_y.append(temp[1])
print(p_x[0], p_y[0])

