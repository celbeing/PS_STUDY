import sys
from math import log10
input = sys.stdin.readline
N,M = map(int,input().split())
S,E = map(int,input().split())
G = abs(S-E)
if N == 2:
    if M % 2 == 0: print(0)
    else: print(1)
elif G > M: print(0)
else:
    result = 0
    n1 = log10(N-1)*M
    for i in range(0,M-G+1):
        n2 = log10(N-2)*(M-G-i)
        result += 10**(n2-n1)
    print(result)