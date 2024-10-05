import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    K = list(map(int, input().split()))
    S = sum(K)
    res = S
    lim = S // 2
    stack = [0]
    for k in K:
        new = []
        while stack:
            new.append(stack.pop())
            if new[-1] + k <= lim:
                new.append(new[-1] + k)
        stack += new
    stack.sort()
    print(S-stack[-1])
solution()