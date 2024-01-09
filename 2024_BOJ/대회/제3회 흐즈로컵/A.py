#A: 이상한 섞기 연산
import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    B = int(input())
    if B < 3:
        print(1)
    else:
        print(3)