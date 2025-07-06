# 2672: 여러 직사각형의 전체 면적 구하기
import sys
input = sys.stdin.readline

def get_data():
    x, y, w, h = map(float, input().split())
    return int(x * 10), int(y * 10), int(w * 10), int(h * 10)

n = int(input())
sweep = [0] * 20001

rects = []
for i in range(n):
    x, y, w, h = get_data()
    rects.append((x, y, h, 1))
    rects.append((x + w, y, h, -1))
rects.sort()

dx, dy, res = 0, 0, 0
for i in range(n * 2):
    x, y, h, d = rects[i]
    res += dy * (x - dx)
    dx = x
    for j in range(y, y + h):
        sweep[j] += d
        if d == -1 and sweep[j] == 0: dy -= 1
        elif d == 1 and sweep[j] == 1: dy += 1
if res % 10:
    print(res / 100)
elif res % 100:
    print(str(res / 100)+'0')
else:
    print(res // 100)