n = 1000

sum = 0
i = 0
for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum + i
        print(sum)
    i += 1
