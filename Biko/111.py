# 111: 사진작가
import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    check = [-1] * 1000001

    l = 0
    res = 0
    for r in range(n):
        if check[a[r]] >= 0:
            for k in range(l, check[a[r]]):
                check[a[k]] = -1
            l = check[a[r]] + 1
        check[a[r]] = r
        res = max(res, r - l + 1)
    print(res)
solution()