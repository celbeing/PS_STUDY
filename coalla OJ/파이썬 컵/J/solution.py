n = int(input())
d = 0
for i in range(1, n):
    if n % i == 0:
        d += i
if d < n:
    print("부족수")
elif d > n:
    print("과잉수")
else:
    print("완전수")