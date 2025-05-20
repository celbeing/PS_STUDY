# 13025: 숫자 골라내기
import sys
input = sys.stdin.readline
def solution():
    l, r, k = map(int, input().split())
    if k == 1:
        print(l)
        print(1)
        print(l)
    elif k == 2:
        if l & 1:
            print(l)
            print(1)
            print(l)
        else:
            print(1)
            print(2)
            print(l, l + 1)
solution()