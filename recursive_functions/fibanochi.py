
# fibonacci recursive effective but not efficient
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(0, 36):
    print(i, fibonacci(i))

