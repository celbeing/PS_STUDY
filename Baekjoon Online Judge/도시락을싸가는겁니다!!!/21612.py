# 21612: Boiling Water
import sys
input = sys.stdin.readline
def solution():
    p = int(input()) * 5 - 400
    print(p)
    if p > 100: print(-1)
    elif p < 100: print(1)
    else: print(0)
solution()