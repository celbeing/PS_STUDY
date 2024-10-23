#30792: ahui and sousenkyo 2
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    v = int(input())
    rank = sorted(list(map(int, input().split())), reverse = True)
    cnt = 1
    for r in rank:
        if r > v: cnt += 1
        else: break
    print(cnt)
solution()