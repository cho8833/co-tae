table = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

total = 0
grade = 0
for _ in range(20):
    s = input().split(' ')
    if s[2] == "P":
        continue
    total += float(s[1])
    grade += float(s[1]) * table[s[2]]

print(grade/total)
    
    
    
