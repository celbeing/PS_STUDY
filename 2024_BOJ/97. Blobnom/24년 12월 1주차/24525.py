# 24525: SKK 문자열
import sys
input = sys.stdin.readline
def solution():
    S = list(input().rstrip())
    n = len(S)
    s = [0] * n
    k = [0] * n
    for i in range(n):
        s[i] = s[i - 1]
        k[i] = k[i - 1]
        if S[i] == 'S':
            s[i] += 1
        elif S[i] == 'K':
            k[i] += 1
        