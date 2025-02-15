# 5375: 공책 구매
import sys
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        notes = [tuple(map(int, input().split())) for _ in range(m)]
        notes.sort(key = lambda x: x[1] + x[2] / x[0])
        cost = 0
        for s, p, o in notes:
            if 
solution()