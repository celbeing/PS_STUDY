import sys
input = sys.stdin.readline
N = int(input())
stack = [100001]

for i in range(N):
    stick = int(input())
    while stack[-1] <= stick:
        stack.pop()
    stack.append(stick)


print(len(stack)-1)

