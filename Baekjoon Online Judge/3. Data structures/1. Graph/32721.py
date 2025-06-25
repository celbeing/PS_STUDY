# 32721: 완벽한 도시 설계
import sys
input = sys.stdin.readline
n = int(input())
a = [0] + list(map(int, input().split()))
indeg = [0] * (n + 1)
for i in range(1, n + 1):
    indeg[a[i]] += 1
check = [1] * (n + 1)
count = 0
for i in range(1, n + 1):
    if indeg[i] == 0:
        k = i
        while check[k]:
            check[k] = 0
            k = a[k]
        count += 1
island = 0
for i in range(1, n + 1):
    if check[i]:
        k = i
        while check[k]:
            check[k] = 0
            k = a[k]
        island += 1
if count == 0 and island == 1: print(0)
else: print(count + island)