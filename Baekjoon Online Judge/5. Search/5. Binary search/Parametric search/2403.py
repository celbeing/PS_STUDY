# 2403: 게시판 구멍 가리기
import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    dots = []
    left, right, top, bottom = 30000, -30000, -30000, 30000
    for _ in range(n):
        x, y = map(int, input().split())
        dots.append((x, y))
        if left > x: left = x
        if right < x: right = x
        if top < y: top = y
        if bottom > y: bottom = y

    s, e, flag, dir = 1, max(right - left, top - bottom), 0, 0
    while s < e:
        m = (s + e) // 2
        flag = 0

        # flag == 1
        for x, y in dots:
            if (left <= x <= left + m and bottom <= y <= bottom + m) or (right - m <= x <= right and top - m <= y <= top):
                continue
            else: break
        else:
            flag = 1
            dir = 1

        # flag == -1
        for x, y in dots:
            if (left <= x <= left + m and top - m <= y <= top) or (right - m <= x <= right and bottom <= y <= bottom + m):
                continue
            else: break
        else:
            flag = -1
            dir = -1

        if flag: e = m
        else: s = m + 1

    print(s)
    if dir == 1:
        print(left, bottom)
        print(right - s, top - s)
    else:
        print(left, top - s)
        print(right - s, bottom)

solution()