#23742: Player-based Team Distribution
import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    A = sorted(list(map(int, input().split())), reverse = True)
    res = 0
    prefix = 0
    k = 0
    for a in A:
        k += 1
        prefix += a
        res = max(prefix * k, res + a)
    print(res)
solution()