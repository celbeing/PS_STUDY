import sys
input = sys.stdin.readline

def sol():
    n = int(input())
    res = 0
    for _ in range(n):
        res += int(input())
    print(res)
sol()