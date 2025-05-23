# 1721: 최대 HP
import sys
input = sys.stdin.readline
def solution():
    h, t = map(int, input().split())
    for _ in range(t):
        a, k = map(int, input().split())
        if a == 1:
            h -= k
        elif a == 2:
            h += k
        else:
            h += k
            print(h)
            break
solution()