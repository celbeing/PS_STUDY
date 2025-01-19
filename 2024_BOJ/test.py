import sys
input = sys.stdin.readline
def solution():
    d = dict()
    for _ in range(int(input())):
        n = int(input())
        d[n] = d.get(n, 0) + 1
    s = sorted(d)
    print(s)
solution()