import sys
input = sys.stdin.readline
N = int(input())-1
if N == 0: print(0)
else:
    p = 9
    digit = 1
    while N > p:
        N -= p
        digit += 1
        if N <= p: break
        N -= p
        digit += 1
        p *= 10
    f = 10 ** ((digit-1)//2)
    N -= 1
    if N > 0:
        f += N
    result = f * (10 ** (digit//2))
    p = 10**((digit-1)//2)
    t = 1
    for i in range((digit)//2):
        result += f//p*t
        f %= p
        p //= 10
        t *= 10
    print(result)