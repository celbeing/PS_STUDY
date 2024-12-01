# 1827: 여행가이드
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    velocity = float(input())
    people = [list(map(float, input().split())) for _ in range(n)]
    