import sys
input = sys.stdin.readline
def solution():
    L = int(input())
    T = int(input())
    print(abs((L - T) - T))
solution()