import sys
input = sys.stdin.readline
def solution():
    N = list(input().rstrip())
    res = 0
    for k in N:
        if k == "A":
            res += 1
    print(res, ":", len(N) - res)
solution()