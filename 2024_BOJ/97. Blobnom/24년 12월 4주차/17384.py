# 17384: 대진표
import sys
input = sys.stdin.readline
write = sys.stdout.write
def solution():
    n = int(input())
    if n == 1:
        write('#.')
        return
    memo = [''] * (n + 1)
    memo[1] = "#"
    def dq(k):
        if memo[k]: return memo[k]

        if k & 1:
            if memo[k // 2 + 1] == '': memo[k // 2 + 1] = dq(k // 2 + 1)
            if memo[k // 2] == '': memo[k // 2] = dq(k // 2)
            memo[k] = memo[k // 2 + 1] + memo[k // 2] + '.' * (len(memo[k // 2 + 1]) - len(memo[k // 2]))
        else:
            if memo[k // 2] == '': memo[k // 2] = dq(k // 2)
            memo[k] = memo[k // 2] * 2
        return memo[k]
    write(dq(n))
solution()