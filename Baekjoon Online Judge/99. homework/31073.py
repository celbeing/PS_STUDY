# 31073: 카탈란 게임
import sys
input = sys.stdin.readline
n = int(input())
p = list(input().strip())
a = [0] * n
a[0] = 1 if p[0] == '(' else -1
for i in range(1, n): a[i] = a[i - 1] + (1 if p[i] == '(' else -1)
flag = True
if n > 1 and n & 1:
    s, e = n // 2 - 1, n // 2
    m = min(a[s], a[e])
    while s >= 0:
        m = min(m, min(a[s], a[e]))
        if a[s] - a[e] == 1 and a[e] >= m:
            flag = False
            break
        s -= 1
        e += 1
    if flag:
        s, e = n // 2, n // 2 + 1
        m = min(a[s], a[e])
        while e < n:
            m = min(m, min(a[s], a[e]))
            if a[s] - a[e] == 1 and a[e] >= m:
                flag = False
                break
            s -= 1
            e += 1
print('junhui' if flag else 'jimin')