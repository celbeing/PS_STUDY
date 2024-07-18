import sys
input = sys.stdin.readline
from fractions import Fraction
tt = "PQWERTYUIOJ#SZK*?F@D!HNM&LXGABCV"
def binary(f):
    x = Fraction(f)
    x1 = x//1
    x2 = x - x1
    dig = ""
    if x1 < 0: dig += "1"
    else: dig += "0"
    for _ in range(16):
        x2 *= 2
        if x2 < 1: dig += "0"
        else:
            dig += "1"
            x2 -= 1
    return dig

for _ in range(int(input())):
    D = float(input())
    if not -1 <= D < 1:
        print("INVALID VALUE")
        continue
    word = binary(D)
    s = tt[int("0b"+word[:5],2)]
    m = int("0b"+word[5:],2)
    e = tt[int("0b"+word[-5:],2)]
    print(s,m,e)