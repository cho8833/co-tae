temp = []
for _ in range(50):
    temp.append(set())
for _ in range(int(input())):
    s = input()
    temp[len(s)-1].add(s)
for data in temp:
    sl = sorted(list(data))
    for s in sl:
        print(s)
