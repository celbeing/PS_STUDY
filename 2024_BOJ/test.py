import sys
input = sys.stdin.readline
def solution():
    P = int(input())
    C = int(input())
    F = P * 50 - C * 10
    F += 500 if P > C else 0
    print(F)
solution()