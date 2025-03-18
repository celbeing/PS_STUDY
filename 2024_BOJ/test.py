import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    x, y = map(int, input().split())
    if n == 1:
        print(0)
        return
    if (x == 1 or x == n) and (y == 1 or y == n):
        print(2)
    elif (x == 1 or x == n) or (y == 1 or y == n):
        print(3)
    else:
        print(4)
    return
solution()