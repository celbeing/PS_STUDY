# 31073: 카탈란 게임
import sys
input = sys.stdin.readline
n = int(input())
s = list(input().strip())

def catalan(i, s, n):
    low_left, low_right = 0, 0
    now_left, now_right = 0, 0
    idx_left, idx_right = i, i + 1
    for _ in range(n):
        now_left += 1 if s[idx_left] == ')' else -1
        now_right += 1 if s[idx_right] == '(' else -1
        if low_left > now_left: low_left = now_left
        if low_right > now_right: low_right = now_right
        idx_left -= 1
        idx_right += 1

        if now_left == now_right and low_left >= now_left and low_right >= now_right:
            return True
    return False
if n & 1:
    n >>= 1
    print('jimin' if catalan(n - 1, s, n) or catalan(n, s, n) else 'junhui')
else:
    print('junhui')