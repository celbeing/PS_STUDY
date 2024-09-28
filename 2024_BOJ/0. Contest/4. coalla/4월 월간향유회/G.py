# 26042: 식당 입구 대기 줄
import sys
input = sys.stdin.readline
n = int(input())
l,s = 0,100000
wait = []
now = 0
for _ in range(n):
    a = list(map(int,input().split()))
    if a[0] == 2:
        now += 1
    else:
        wait.append(a[1])
        if len(wait)-now == l and s > wait[-1]:
            s = wait[-1]
        elif len(wait)-now > l:
            l = len(wait)-now
            s = wait[-1]
print(l,s)