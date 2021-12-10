num = []
sum1 = 0
sum2 = 0
for i in range(1, 1000, 2):
    num.append(i**3)
for idx in range(len(num)):
    sum_num = 0
    per = num[idx]
    while per:
        sum_num += per % 10
        per = per // 10
    if sum_num % 7 == 0:
        sum1 += num[idx]
    num[idx] += 17
    sum_num = 0
    per = num[idx]
    while per:
        sum_num += per % 10
        per = per // 10
    if sum_num % 7 == 0:
        sum2 += num[idx]
print(sum1)
print(sum2)
