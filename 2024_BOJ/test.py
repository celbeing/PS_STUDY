import sys
input = sys.stdin.readline
def solution():
    n = input().strip()
    res = "1"
    k = 2
    while int(res) < int(n):
        res += str(k)
        k += 1
    if res == n:
        print(k - 1)
    else: print(-1)
solution()