import sys
input = sys.stdin.readline
def solution():
    k = tuple(map(int, input().split())) + (4)
    print(k)
solution()