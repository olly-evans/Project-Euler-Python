# nth prime number.
n = 10001


# is number prime?
def isPrime(p):
    # Check numbers less than 2. And rule out even numbers.
    if p < 2:
        return False
    elif p != 2 and p % 2 == 0:
        return False
    

    for i in range(2, p):
        if (p % i) == 0:
            return False
    return True

k = 1
count = 0
while True:
    if isPrime(k):
        count += 1


    if count == n:
        print(k)
        break
    k += 1
