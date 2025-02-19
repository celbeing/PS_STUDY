# 31537: 출근하기 싫어 1
import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    mod = int(1e9 + 7)
    a = list(map(int, input().split()))
    perf = [0] * (m + 1)
    abse = [1] * (m + 1)
    perf[0] = 1
    for k in a:
        for i in range(1, k + 1):
