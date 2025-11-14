n = int(input())
tri = []
while n:
    tri.append(n % 3)
    n //= 3
res = 0
while tri:
    res *= 10
    res += tri.pop()
print(res)