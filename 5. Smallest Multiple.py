i = 20
while True:
    counter = 0
    for j in range(1, 21):
        if i % j == 0:
            counter += 1

    if counter == 20:
        print(i)
        break
    i += 10

# 232792560
