# 27962: 오렌지먹은지오랜지
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    s = input().strip()
    for i in range(1, n):
        a = s[:n - i]
        b = s[i:]
        c = 0
        for j in range(n - i):
            if a[j] == b[j]: continue
            if c == 0: c += 1
            else:
                c += 1
                break
        if c == 1:
            print('YES')
            return
    print('NO')
solution()