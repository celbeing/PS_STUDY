import sys
input = sys.stdin.readline
N = int(input())
power = 0
stack = []
for i in range(N):
    p = int(input())
    if stack:
        if p > stack[-1]:
            stack.append(p)
        else:
            stack.clear()
            print(i)
            
    else:
        stack.append(p)