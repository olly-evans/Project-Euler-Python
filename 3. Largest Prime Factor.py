def main():
    # 600851475143
    n = 600851475143
    for i in range(2, n):
        if i >= n:
             break
        elif n % i == 0 and isprime(i) == True:
                n = int(n / i)

    print(n)

def isprime(p):
    for i in range(2, p):
        if (p % i) == 0:
            return False
    return True

main()
