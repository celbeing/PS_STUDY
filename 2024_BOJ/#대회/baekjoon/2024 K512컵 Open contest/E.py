import sys
input = sys.stdin.readline
Q = int(input())
stack = {}
for _ in range(Q):
    q,i = map(int,input().split())
    if q == 1:
        high = 0
        for j in range(i, i+4):
            if j in stack:
                if stack[j] > high:
                    high = stack[j]
        high += 1
        for j in range(i, i+4):
            stack[j] = high
    elif q == 2:
        if i in stack:
            stack[i] += 4
        else:
            stack[i] = 4
    else:
        if i in stack:
            print(stack[i])
        else:
            print(0)