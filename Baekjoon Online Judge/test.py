import sys
input = sys.stdin.readline

def func(a, b, c, x):
    return a * x ** 2 + b * x  + c

for _ in range(int(input())):
    a, b, c, s, t = map(int, input().split())
    fs, ft = func(a, b, c, s), func(a, b, c, t)
    if fs * ft > 0:
        if a == 0:
            print('No')
        elif b ** 2 > (a * c) << 2:
            if a > 0 and fs < 0:
                print('No')
            elif a < 0 and fs > 0:
                print('No')
            else:
                if s <= -(b / a) / 2 <= t:
                    print('Yes')
                else:
                    print('No')
        else:
            print('No')
    else:
        print('Yes')