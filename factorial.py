def factorial(n):
    x = 1
    li = list(range(1, n + 1))
    for each in li:
        x = x * each
    print(x)

factorial(120)