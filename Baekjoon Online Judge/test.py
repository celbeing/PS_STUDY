import sys
input = sys.stdin.readline

a = sorted(list(map(int, input().split())))
res = a[0] + (a[1] - a[0]) // 3 + (a[2] - a[0]) // 3
if (a[1] - a[0]) % 3: res += 1
if (a[2] - a[0]) % 3: res += 1
if (a[1] - a[0]) % 3 == (a[2] - a[0]) % 3 == 1: res -= 1
print(res)