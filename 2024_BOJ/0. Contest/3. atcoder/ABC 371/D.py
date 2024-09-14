import sys
input = sys.stdin.readline
def binleft(X, k):
    l, r = 0, len(X)
    while l < r:
        m = (l + r) // 2
        if X[m] < k:
            l = m + 1
        elif X[m] == k:
            return m - 1
        else:
            r = m
    return r - 1
def binright(X, k):
    l, r = 0, len(X) - 1
    while l < r:
        m = (l + r + 1) // 2
        if X[m] <= k:
            l = m
        elif X[m] == k:
            return m
        else:
            r = m - 1
    if r == 0 and  X[r] > k:
        return r - 1
    return r
def solution():
    N = int(input())
    X = list(map(int, input().split()))
    P = [0] + list(map(int, input().split()))
    for i in range(2, N + 1):
        P[i] += P[i - 1]
    for _ in range(int(input())):
        L, R = map(int, input().split())
        l = binleft(X, L)
        r = binright(X, R)
        print(P[r+1] - P[l+1])
solution()