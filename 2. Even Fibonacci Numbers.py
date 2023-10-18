n = 1000
fib1 = 1
fib2 = 2

sum = 0
i = 0
for i in range(n):
    if (fib1 + fib2) > 4000000:
        exit()

    print(fib1 + fib2)
    fib_new = fib1 + fib2

    if fib1 % 2 == 0:
        sum += fib1
        print("sum: " + str(sum))

    fib1 = fib2
    fib2 = fib_new
    i += 1

    print("final: " + str(sum + fib_new))
