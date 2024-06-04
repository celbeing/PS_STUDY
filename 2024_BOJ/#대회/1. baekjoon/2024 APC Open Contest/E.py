N = int(input())
result = 9
while N > 0:
    N //= 2
    result += 1
print(result)