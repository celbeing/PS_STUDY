# 25577: 열 정렬정렬 정
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    c = dict()
    for i in range(n):
        c[a[i]] = b[i]
    check = set()
    count = 0
    for k in a:
        check.add(k)
        t = k
        while not c[t] in check:
            t = c[t]
            check.add(t)
            count += 1
    print(count)
solution()