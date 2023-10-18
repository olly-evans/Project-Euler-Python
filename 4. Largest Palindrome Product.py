def main():
    palindromes = []
    counter = 0
    # from x to y - 1
    for l in range(100, 1000):
        for k in range(100, 1000):
            if isPalindrome(l * k):
                palindromes.append(l * k)
                counter += 1
    print("Counter: " + str(counter))
    print(max(palindromes))



def isPalindrome(n):
    n = str(n)
    digits = len(n)

    if digits % 2 == 0:

        # split in half
        index = (digits // 2)

        # not splitting well
        first = n[:index]
        last = n[index:]

        # compare last digit to first. i + 1, j -1.
        i = 0
        j = len(last) - 1
        success = 0
        try:
            while True:
                if first[i] == last[j]:
                    success += 1
                i += 1
                j -= 1
                if i == len(first) and success == (len(n) / 2) and j == -1: # broken conditions, does not like the indexing.
                    break

            return True
        except IndexError:
            return False
    else:
        # remove middle digit at index len / 2
        # S = S[:Index] + S[Index + 1:]
        digits = digits - 1
        middle_index = (len(n) - 1) // 2
        n = n[:middle_index] + n[middle_index + 1:]

        index = (digits // 2)

        # not splitting well
        first = n[:index]
        last = n[index:]

        # compare last digit to first. i + 1, j -1.
        i = 0
        j = len(last) - 1
        success = 0
        try:
            while True:
                if first[i] == last[j]:
                    success += 1
                i += 1
                j -= 1
                if i == len(first) and success == (len(n) / 2) and j == -1: # broken conditions, does not like the indexing.
                    break

            return True
        except IndexError:
            return False

main()
