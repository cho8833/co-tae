m, n = map(int, input().split())
data = []
for _ in range(m):
    data.append(list(input()))

result = 65
for i in range(m-7):
    for j in range(n-7):
        check1 = 'W'
        check2 = 'B'        
        fill1 = 0
        fill2 = 0
        for y in range(i, i+8):
            for x in range(j, j+8):
                if check1 != data[y][x]:
                    fill1 += 1
                if check2 != data[y][x]:
                    fill2 += 1

                if check1 == 'W':
                    check1 = 'B'
                    check2 = 'W'
                else:
                    check1 = 'W'
                    check2 = 'B'
                    
            if check1 == 'W':
                check1 = 'B'
                check2 = 'W'
            else:
                check1 = 'W'
                check2 = 'B'
                
        result = min(fill1, fill2, result)

print(result)
