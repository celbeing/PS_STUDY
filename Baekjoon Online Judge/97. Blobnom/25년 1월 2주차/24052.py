# 24052: 알고리즘 수업 - 삽입 정렬 2
import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(1, n):
        loc = i - 1
        newItem = a[i]
        while loc >= 0 and newItem < a[loc]:
            a[loc + 1] = a[loc]
            loc -= 1
            count += 1
            if count == k:
                print(*a)
                return
        if loc + 1 != i:
            a[loc + 1] = newItem
            count += 1
            if count == k:
                print(*a)
                return
    print(-1)
solution()