N, M = map(int, input().split())

def recur(prev, start, count):
    if count == 1:
        for i in range(start, N+1):
            print(prev + str(i))
    else:
        for i in range(start, N+2-count):
            if prev == "":
                recur(str(i) + " ", i+1, count-1)
            else:
                recur(prev + str(i) + " ",i +1, count-1)
            
recur("", 1, M)
    
