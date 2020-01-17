def factorial(n):
    # n! can also be fined as n * (n-1)

    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


try:
    print(factorial(900))
except (RecursionError, OverflowError):
    print("This program can't calculate factorials that large")

print("Program done")
