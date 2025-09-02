import sys

temp = list(sys.stdin.readline().rstrip())
isbn = []
for s in temp:
    if s != "*":
        isbn.append(int(s))
    else:
        isbn.append(-1)
flag = 1

check_flag = 0

cal = 0
for i in isbn:
    if i != -1:
        cal += i * flag
    else:
        check_flag = flag
    if flag == 1:
        flag = 3
    else:
        flag = 1

for i in range(10):
    if (check_flag * i + cal) % 10 == 0:
        print(i)
        break