# 14492: 부울행렬의 부울곱
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[i][k] and b[k][j]:
                    res += 1
                    break
    print(res)
solution()