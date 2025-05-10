# 2096: 내려가기
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    max_score = list(map(int, input().split()))
    min_score = [0] * 3
    for i in range(3): min_score[i] = max_score[i]

    for _ in range(n - 1):
        line = list(map(int, input().split()))
        ma = line[0] + max(max_score[:2])
        mb = line[1] + max(max_score)
        mc = line[2] + max(max_score[1:])
        max_score = [ma, mb, mc]
        ma = line[0] + min(min_score[:2])
        mb = line[1] + min(min_score)
        mc = line[2] + min(min_score[1:])
        min_score = [ma, mb, mc]
    print(max(max_score), min(min_score))
solution()