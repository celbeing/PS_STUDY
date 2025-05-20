import sys
input = sys.stdin.readline
def solution():
    s = list(input().strip())
    res = ''
    for k in s:
        if ord(k) < 97:
            res += k
    print(res)
solution()