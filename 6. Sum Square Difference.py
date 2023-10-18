def main():
    # choose range
    num = 100

    # subtract
    number = sumSquared(num) - sumOfSquares(num)
    # result
    print(number)

# function to find sum of squares from 1 to k.
def sumOfSquares(k):
    sum = 0
    for i in range(1, k + 1):
        sum += i * i
    return sum

# function to find the sum of numbers from 1 to k, squared.
def sumSquared(k):
    sum = 0
    for i in range(1, k + 1):
        sum += i
    return sum * sum

main()
