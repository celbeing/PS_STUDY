# 20833: Kuber
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    print((n * (n + 1 ) // 2) ** 2)
solution()