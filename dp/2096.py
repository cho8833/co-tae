import sys
N = int(input())

minAnswer = list(map(int, sys.stdin.readline().rstrip().split()))
maxAnswer = minAnswer[:]


for _ in range(N-1):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    temp = [0,0,0]
    temp[0] = row[0] + min(minAnswer[0], minAnswer[1])
    temp[1] = row[1] + min(minAnswer[0], minAnswer[1], minAnswer[2])
    temp[2] = row[2] + min(minAnswer[1], minAnswer[2])
    minAnswer = temp[:]

    temp = [0,0,0]
    temp[0] = row[0] + max(maxAnswer[0], maxAnswer[1])
    temp[1] = row[1] + max(maxAnswer[0], maxAnswer[1], maxAnswer[2])
    temp[2] = row[2] + max(maxAnswer[1], maxAnswer[2])
    maxAnswer = temp[:]

print(max(maxAnswer), min(minAnswer))