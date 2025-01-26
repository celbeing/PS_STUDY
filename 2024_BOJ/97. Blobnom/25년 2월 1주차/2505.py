# 2505: 두 번 뒤집기
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    def left(arr):
        l, r = 0, 0
        for i in range(n):
            if arr[i] != i + 1:
                l = i
                r = arr.index(i + 1) + 1
                return l, r
        return 0, 0

    def right(arr):
        l, r = 0, 0
        for i in range(n - 1, -1, -1):
            if arr[i] != i + 1:
                l = arr.index(i + 1)
                r = i + 1
                return l, r
        return 0, 0

    def turn(arr, l, r):
        p = arr[l:r]
        p.reverse()
        return arr[:l] + p + arr[r:]

    def check(arr):
        for i in range(n):
            if arr[i] != i + 1:
                return 0
        return 1

    if check(arr):
        print(1, 1)
        print(1, 1)
        return

    a, b = left(arr)
    l = turn(arr, a, b)
    if check(l):
        print(a + 1, b)
        print(1, 1)
        return

    c, d = left(l)
    ll = turn(l, c, d)
    if check(ll):
        print(a + 1, b)
        print(c + 1, d)
        return

    c, d = right(l)
    lr = turn(l, c, d)
    if check(lr):
        print(a + 1, b)
        print(c + 1, d)
        return

    a, b = right(arr)
    r = turn(arr, a, b)
    if check(r):
        print(a + 1, b)
        print(1, 1)
        return

    c, d = left(r)
    rl = turn(r, c, d)
    if check(rl):
        print(a + 1, b)
        print(c + 1, d)
        return

    c, d = right(r)
    rr = turn(r, c, d)
    if check(rr):
        print(a + 1, c)
        print(c + 1, d)
        return
solution()