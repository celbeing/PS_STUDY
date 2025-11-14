import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
res = 0
for i in range(n):
    l, r = 0, 0
    for j in range(i - 1, -1, -1):
        if a[j] >= a[i]:
            l = i - j - 1
            break
    for j in range(i + 1, n):
        if a[j] >= a[i]:
            r = j - i - 1
            break
    if res < max(l, r):
        res = max(l, r)
print(res)