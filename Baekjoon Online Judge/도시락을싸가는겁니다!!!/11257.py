# 11257: IT Passport Examination
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    for _ in range(n):
        code, st, ce, tc = input().split()
        st, ce, tc = int(st), int(ce), int(tc)
        total = st + ce + tc
        if st >= 35*0.3 and ce >= 25*0.3 and tc >= 40*0.3 and total >= 55:
            print(code, total, 'PASS')
        else:
            print(code, total, 'FAIL')
solution()