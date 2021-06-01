def fib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fib(num - 1) + fib(num - 2)

print(fib(0))
print(fib(1))
print(fib(5))
print(fib(7))
print(fib(10))
print(fib(12))