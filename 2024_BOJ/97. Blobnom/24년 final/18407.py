# 18407: 가로 블록 쌓기
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    for _ in range(n):
        w, d = map(int, input().split())
        