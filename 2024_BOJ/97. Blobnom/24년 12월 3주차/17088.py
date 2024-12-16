# 17088: 등차수열 변환
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    b = list(map(int, input().split()))
    d = [0] * 9
    c = [-1] * 9
    if b[1] - b[0] % 3 == 0:
        