# 15889: 호 안에 수류탄이야!!
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    cor = list(map(int, input().split()))
    ran = list(map(int, input().split()))
    reach = 0
    for i in range(N - 1):
        if cor[i] <= reach:
            reach = max(cor[i] + ran[i], reach)
        else: break
    if reach >= cor[-1]: print("권병장님, 중대장님이 찾으십니다")
    else: print("엄마 나 전역 늦어질 것 같아")
solution()