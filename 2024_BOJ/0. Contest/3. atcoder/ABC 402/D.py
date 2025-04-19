import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    count = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        count[(b + a - 2) % n] += 1
    pre = [0] * (n + 1)
    pre[0] = count[0]
    for i in range(1, n + 1):
        pre[i] = pre[i - 1] + count[i]
    res = 0
    for i in range(n):
        res += count[i] * (pre[-1] - pre[i])
    print(res)
solution()