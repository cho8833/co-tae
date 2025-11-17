N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

answer = []

while True:
    if not A or not B:
        break
    temp = set(A) & set(B)
    if not temp:
        break
    
    mx = max(temp)
    answer.append(mx)
    A = A[A.index(mx)+1:]
    B = B[B.index(mx)+1:]


print(len(answer))
print(" ".join(map(str, answer)))