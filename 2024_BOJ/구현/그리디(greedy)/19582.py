# 19528: 200년간 폐관수련했더니 PS 최강자가 된 건에 대하여
import sys
input = sys.stdin.readline
N = int(input())
sum = 0
max = 0
passed = 0
for _ in range(N):
    x,p = map(int,input().split())
    if sum <= x:
        sum += p
        if max < p:
            max = p
    elif sum-max > x or max < p:
            passed += 1
    else:
        passed += 1
        sum -= max
        sum += p
if passed < 2:
    print("Kkeo-eok")
else:
    print("Zzz")