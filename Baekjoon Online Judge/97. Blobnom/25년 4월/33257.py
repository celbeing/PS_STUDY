# 33257: 상현이의 물리학및실험1 실험 대작전
import sys
input = sys.stdin.readline
def solution():
    n, e = map(int, input().split())
    d = sorted(list(map(int, input().split())))
    count = 1
    for i in range(1, n):
        if d[i] - d[i - 1] > e:
            count += 1
    print(count)
solution()