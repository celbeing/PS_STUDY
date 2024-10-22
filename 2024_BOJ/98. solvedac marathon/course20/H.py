#13713: 문자열과 쿼리
import sys
input = sys.stdin.readline
def solution():
    S = list(input().strip())
    S.reverse()
    l, r = 0, 0
    n = len(S)
    Z = [0] * n
    Z[0] = n
    for i in range(1, n):
        if i <= r: Z[i] = min(r - i, Z[i - l])
        while i + Z[i] < n and S[i + Z[i]] == S[Z[i]]: Z[i] += 1
        if i > r: l = i
        r = max(r, i + Z[i] - 1)
    for _ in range(int(input())):
        print(Z[n - int(input())])
solution()