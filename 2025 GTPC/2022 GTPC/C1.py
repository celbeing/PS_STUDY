a, b, k = map(int, input().split())
res = a // b
a %= b
for _ in range(k):
    a *= 10
    res *= 10
    res += a // b
    a %= b
a *= 10
if a // b >= 5: res += 1
print(f'{res // 10**k}.{res%10**k}')