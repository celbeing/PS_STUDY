#G: 어려운 정수 맞히기 게임
import sys

n = int(input())
for _ in range(n):
    a,b = 0,0
    r = '+'
    s, e = 0, 1e9
    count = 0
    last = e
    while True:
        m = int(((s**2+e**2)//2)**0.5)
        print("? {} {}".format(int(a),int(m)))
        sys.stdout.flush()
        count += 1
        result = input().rstrip()
        if result == '+':
            a += m**2
            s = 0
            e = int((last**2-m**2)**0.5)
            last = e
        elif result == '-':
            e = m-1
            last = m
        else:
            b = m
            break

    print("! {}".format(int(a+b**2)))
    sys.stdout.flush()