import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    res = []
    for i in range(1,N+1):
        res.append(i)
        if i % 6 == 0:
            res.append("Go!")
    if N % 6: res.append("Go!")
    print(*res)
sol()