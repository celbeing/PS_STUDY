# 13413: 오셀로 재배치
import sys
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        n = int(input())
        origin = list(input().strip())
        finish = list(input().strip())
        a, b = 0, 0
        for i in range(n):
            if origin[i] != finish[i]:
                if origin[i] == 'W': a += 1
                else: b += 1
        print(max(a, b))
solution()