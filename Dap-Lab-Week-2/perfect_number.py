def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n


num = 28
print(is_perfect(num))
