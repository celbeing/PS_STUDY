# 1838: 버블 정렬
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
idx = dict()
for i in range(n):
    idx[a[i]] = i
a.sort()
moved = 0
for i in range(n):
    moved = max(moved, idx[a[i]] - i)
print(moved)