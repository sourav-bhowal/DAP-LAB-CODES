def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


num = 1234
print(sum_of_digits(num))
