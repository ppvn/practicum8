n = int(input())
for i in range(1, n+1):
    k = 0
    for j in range(1, i+1):
        if i % j == 0:
            k += j
    if k == 2*i:
        print(i)