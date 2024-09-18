#8891: 점 숫자
import sys
input = sys.stdin.readline
def solution():
    dot = dict()
    cor = dict()
    x, y = 1, 1
    for d in range(1, 40162):
        dot[d] = (x, y)
        cor[(x, y)] = d
        if y == 1:
            y = x + 1
            x = 1
        else:
            x += 1
            y -= 1
    for _ in range(int(input())):
        a, b = map(int, input().split())
        ax, ay = dot[a]
        bx, by = dot[b]
        print(cor[(ax + bx, ay + by)])
solution()