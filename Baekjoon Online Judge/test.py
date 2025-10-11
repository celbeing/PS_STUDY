import sys
input = sys.stdin.readline

t = int(input())
s = list(map(int, input().split()))

while len(s) < 5: s.append(0)
res = 0
if s[0] > s[2]: res += (s[0] - s[2]) * 508
else: res += (s[2] - s[0]) * 108

if s[1] > s[3]: res += (s[1] - s[3]) * 212
else: res += (s[3] - s[1]) * 305

res += s[4] * 707
res *= 4763

print(res)