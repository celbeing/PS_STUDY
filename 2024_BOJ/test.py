import sys
input = sys.stdin.readline
def solution():
    l = [int(input()) for _ in range(4)]
    print((l[1]+l[3]+max(l[0],l[2]))*2+4)
solution()