from math import sin, cos, atan2, pi
for _ in range(int(input())):
    c = int(input())
    a, b = map(float, input().split())
    if c == 1:
        r = (a * a + b * b) ** 0.5
        print(r, atan2(b, a) % (pi * 2))
    else:
        print(a * cos(b), a * sin(b))