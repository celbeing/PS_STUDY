# 17452: Christmalo.win
import sys
input = sys.stdin.readline
def solution():
    abc = 'abcdefghijklmnopqrstuvwxyz'
    F = [50] * 26
    B = [50] * 26
    res = 50
    for i in range(int(input())):
        s = input().strip()
        for j in range(26):
            f = s.find(abc[j])
            b = len(s) - s.rfind(abc[j]) - 1
            if f >= 0:
                res = min(res, min(f + B[j], b + F[j]))
                F[j] = min(F[j], f)
                B[j] = min(B[j], b)
    if res == 50:
        print(-1)
    else:
        print(res)
solution()