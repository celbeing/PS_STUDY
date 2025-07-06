# 2527: 직사각형
import sys
input = sys.stdin.readline

def check():
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    if (x1 == p2 and y1 == q2) or (x2 == p1 and y2 == q1) or (x1 == p2 and y2 == q1) or (x2 == p1 and y1 == q2): print('c')
    elif ((x1 == p2 or x2 == p1) and not(y1 > q2 or y2 > q1)) or ((y1 == q2 or y2 == q1) and not(x1 > p2 or x2 > p1)): print('b')
    elif area(x1, y1, p1, q1, x2, y2, p2, q2): print('a')
    else: print('d')

def area(x1, y1, p1, q1, x2, y2, p2, q2):
    return max(min(p1, p2) - max(x1, x2), 0) * max(min(q1, q2) - max(y1, y2), 0)

for _ in range(4): check()