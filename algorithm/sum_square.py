def sum_square(n):
    sum = 0
    for i in range(1, n+1):
        sum += n * n
        return sum

print(sum_square(3))
print(sum_square(10))