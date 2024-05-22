while True:
    n = float(input())
    if n == 0: break
    result = 1
    result += n
    result += n**2
    result += n**3
    result += n**4
    print("{:.2f}".format(result))