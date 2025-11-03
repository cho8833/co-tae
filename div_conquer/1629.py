A, B, C = map(int, input().split())

def div_conquar(b):
    global A
    global C

    if b == 0: 
        return 1
    if b == 1: 
        return A % C
    
    temp = div_conquar(b // 2) % C

