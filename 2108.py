import sys
n_sum = 0

max_n = -4001
min_n = 4001
nn = int(input())

median_temp = 0
median = -4001

density = [0] * 8002
for _ in range(nn):
    n = int(sys.stdin.readline())
    n_sum += n
    density[n] += 1

max_den = 0
max_den_values = []
for i in range(-4000, 4001, 1):
    if density[i] != 0:
        max_n = max(i, max_n)
        min_n = min(i, min_n)
        if density[i] > max_den:
            max_den = density[i]
            max_den_values = [i]
        elif density[i] == max_den:
            max_den_values.append(i)

        median_temp += density[i]
        if median_temp > nn//2 and median == -4001:
            median = i
    
print(round(n_sum / nn))
print(median)
if len(max_den_values) > 1:
    print(max_den_values[1])
else:
    print(max_den_values[0])
print(max_n - min_n)
