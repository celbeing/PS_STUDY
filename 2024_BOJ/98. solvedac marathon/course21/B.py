#19788: Болезнь
import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    vir = [[0] * 3 for _ in range(n + 1)]
    for _ in range(m):
        data = list(map(int, input().split()))
        if data[-1]:

