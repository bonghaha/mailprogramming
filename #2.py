def evenFibSum(n):
    sum = 0
    x = 1
    y = 2
    while x <= n:
        if x % 2 == 0:
            sum += x
        z = x + y
        x = y
        y = z
    return sum

n = 12
print(evenFibSum(n))