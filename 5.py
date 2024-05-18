x = int(input())
k = 0
for i in range(2, x+1):
    sm = 0
    for j in range(1, i+1):
        if i%j == 0:
            sm += j
    if sm == 2*i:
        k += 1
print(k)