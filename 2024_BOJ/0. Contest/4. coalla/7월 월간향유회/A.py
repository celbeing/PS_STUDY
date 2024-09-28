#1783: 병든 나이트
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
maximum = 1
if N > 1 and M > 1:
    if N == 2:
        if 3 <= M < 5: maximum = 2
        elif 5 <= M < 7: maximum = 3
        elif 7 <= M: maximum = 4
    else:
        if M < 3: maximum = 2
        elif 3 <= M < 4: maximum = 3
        elif 4 <= M < 7: maximum = 4
        elif 7 <= M: maximum = M - 2
print(maximum)