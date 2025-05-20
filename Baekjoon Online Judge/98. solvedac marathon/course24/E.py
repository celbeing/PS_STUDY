# 23257: 비트코인은 신이고 나는 무적이다
import sys
input = sys.stdin.readline
miis = lambda: map(int, input().split())
def solution():
    N, M = miis()
    A = list(abs(a) for a in miis())
    A_set = set(A)
    for _ in range(M - 1):
        A_set = set(i ^ j for i in A for j in A_set)
    print(max(A_set))
solution()