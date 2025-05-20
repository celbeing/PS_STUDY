# 26087: 피보나치와 마지막 수열과 쿼리
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    Q = int(input())
    query = [tuple(map(int, input().split())) for _ in range(Q)]
    fib = [0] * (N + 1)
    fib[0] = 1
    fib[1] = 1
    for i in range(2, N + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % 1000000007

    head = [i for i in range(N + 1)]

    def find(k):
        r = k
        while head[r] != r:
            r = head[r]
        while head[k] != k:
            t = head[k]
            head[k] = r
            k = t
        return k

    res = [0] * N
    for l, r in reversed(query):
        l -= 1; r -= 1
        k = l
        while True:
            if res[k] == 0:
                res[k] = fib[k - l + 1]
            k = find(k) + 1
            if k <= r:
                head[k - 1] = k
            else:
                break
    print(*res)
solution()