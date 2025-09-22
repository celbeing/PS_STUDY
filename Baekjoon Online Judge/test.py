import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    s = list(input().strip())
    res = 0
    tmp = 0
    for i in range(n):
        if s[i] in {'.', '|', ':', '#'}:
            res += tmp
            tmp = 0
        else:
            tmp *= 10
            tmp += int(s[i])
    if res: res += tmp
    print(res)
solution()