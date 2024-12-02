import sys
input = sys.stdin.readline
def solution():
       N, W, H, L = map(int, input().split())
       print(min(N,(W // L) * (H // L)))
solution()