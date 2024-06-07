#B: 자작나무가 없소~
import sys
input = sys.stdin.readline
N,S = input().split()
N = int(N)
count = 0
for _ in range(N):
    item = input().split()
    k = int(item[-1])
    item = item[0].split('_')
    if S in item:
        count += k
print(count)