import sys
input = sys.stdin.readline
def solution():
    A, P = map(int, input().split())
    A *= 7
    P *= 13
    if A > P: print("Axel")
    elif A < P: print("Petra")
    else: print("lika")
solution()