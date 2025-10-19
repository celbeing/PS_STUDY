import sys
input = sys.stdin.readline
n = int(input())
ufo = [tuple(map(float, input().split())) for _ in range(n)]
a, b = map(float, input().split())
res = 0
for x, y, r in ufo:
    if y <= a*x+b: res += 1
print(res)