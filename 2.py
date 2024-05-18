best_score = 0
count = 0
while True:
    score = int(input())
    if score == -1:
        break
    else:
        count += 1
    if score > best_score:
        best_score = score
print(count)
