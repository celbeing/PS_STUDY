import sys
input = sys.stdin.readline
def solution():
    N, Q = map(int, input().split())
    port = [0] * (N + 1)
    jump = [i for i in range(1, N + 1)]
    for q in range(1, Q + 1):
        t, i = map(int, input().split())
        k = i
        if t == 1:
            while i <= N and port[i]:
                i = jump[i]
            if i > N: print(-1)
            else:
                jump[k] = i + 1
                port[i] = q
                print(i)
        else:
            print(port[i] if port[i] else -1)
            port[i] = 0
solution()