import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    i, j = 0, 0
    s = 0
    res = 0
    while j < N:
        if s < N:
            j += 1
            s += j
        elif s > N:
            s -= i
            i += 1
        else:
            res += 1
            j += 1
            s += j
    print(res)

sol()