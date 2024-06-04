# B: 예비 소집 결과 보고서
import sys
input = sys.stdin.readline
N = int(input())
count = 0
for _ in range(N):
    T = list(map(int,input().split()))
    for i in range(3):
        if T[i] == -1: T[i] = 121
    if T[0] < 121 and T[0] <= T[1] <= T[2]: count += 1
print(count)