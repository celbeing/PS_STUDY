# 17384: 대진표
import sys
input = sys.stdin.readline
write = sys.stdout.write
def solution():
    n = int(input())
    memo = [''] * (n + 1)
    memo[1] = "#"
    def dq(k):
        if k == 1: return '#'
        if memo[k]: return memo[k]
        b = 1
        while b < k: b <<= 1
        d = (b * 3) // 4
        b >>= 1
        if k > d:
            memo[b] = dq(b)
            memo[k - b] = dq(k - b)
            return memo[b] + memo[k - b]
        else:
            b >>= 1
            memo[k - b] = dq(k - b)
            memo[b] = dq(b)
            return memo[k - b] + memo[b] + '.' * b
    write(dq(n))
solution()