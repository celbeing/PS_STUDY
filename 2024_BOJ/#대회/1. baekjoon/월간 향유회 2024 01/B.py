#B번 - 캬루
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, P = map(int,input().split())
    if P <=5 :
        print(*[6, 3])
        continue
    dsum = 0
    digit = [0]*N
    t = 1
    for i in range(N):
        digit[i] = (P // t) % 10
        dsum += digit[i]
        t *= 10
    lower = dsum % 3
    upper = 3 - lower
    t = 1
    for i in range(N):
        if digit[i] <= lower:
            print(*[P+t*upper, 3])
        else:
            print(*[P-t*lower, 3])
        t *= 10