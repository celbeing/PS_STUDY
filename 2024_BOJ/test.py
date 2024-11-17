def fib(n):
    ret = 1
    if n < 2:
        return (n, 1)
    a, b = fib(n - 2)
    c, d = fib(n - 1)
    return (a + c, (ret + b + d) % 1000000007)
n = int(input())
f, c = fib(n)
print(f, c)