import sys
input = sys.stdin.readline

n = int(input()) - 1
a = sorted(list(map(int, input().split())))
count = 0
while 1:
    count += min(a[n] + a[n - 1] + a[0] * 2, a[n] + a[0] + a[1] * 2)
    n -= 2
    if n < 3:
        if n == 2: count += a[0] + a[1] + a[2]
        if n == 1: count += a[1]0.

        if n == 0: count += a[0]
        break

print(count)