length = int(input())

data = list(map(int, input().split()))
data.sort()

input()

target = list(map(int, input().split()))

for n in target:
    start = 0
    end = length-1

    while start + 1 < end:
        mid = (start + end) / 2
        