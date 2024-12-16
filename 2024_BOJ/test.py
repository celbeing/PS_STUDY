import sys
input = sys.stdin.readline
def solution():
    c = 0
    for _ in range(int(input())):
        d = int(input().lstrip('D-'))
        if d <= 90:
            c += 1
    print(c)
solution()