# 10703: 유성
import sys
input = sys.stdin.readline
def solution():
    r, s = map(int, input().split())
    photo = [list(input().rstrip()) for _ in range(r)]
    dist = r
    for i in range(s):
        d = 0
        t = r - 1
        while photo[t][i] == '#': t -= 1
        while t >= 0 and photo[t][i] != 'X':
            if photo[t][i] == '#':
                d = -1
            d += 1
            t -= 1
        if t != -1 and dist > d: dist = d
    for j in range(s):
        for i in range(r - 1, -1, -1):
            if photo[i][j] == 'X':
                photo[i][j] = '.'
                photo[i + dist][j] = 'X'
    for line in photo:
        print(''.join(line))
solution()