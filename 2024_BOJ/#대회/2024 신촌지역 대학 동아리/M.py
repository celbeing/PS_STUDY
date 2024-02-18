# M: 엘리스 트랙 매칭
import sys
input = sys.stdin.readline
N = int(input())
track = list(input().split())
hello = input().rstrip()
count = 0
for k in track:
    if hello == k:
        count += 1
print(count)