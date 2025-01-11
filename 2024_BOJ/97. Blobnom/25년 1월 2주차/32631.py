# 32631: 두 덱
import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        a[i] += a[i - 1]
        b[i] += b[i - 1]
    res = max(a[-1], b[-1])
    A = [a[-1]] * (k + 1)
    B = [b[-1]] * (k + 1)
    for i in range(n - k, n + 1):
        for j in range(n - i):
            A[i - n + k] = min(A[i - n + k], a[i + j] - a[j])
            B[i - n + k] = min(B[i - n + k], b[i + j] - b[j])
    for i in range(k + 1):
        for j in range(k - i, k + 1):
            res = min(res, max(A[i], B[j]))
    print(res)
solution()