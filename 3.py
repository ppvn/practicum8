total_income = 0
count = 0
while True:
    income = int(input())
    if income == 0:
        break
    if income > 0:
        total_income += income
        count += 1
if count > 0:
    average_income = total_income / count
print(average_income)