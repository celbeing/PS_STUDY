import sys
input = sys.stdin.readline
N = int(input())
mine = [0]+[int(input()) for  _ in range(N)]+[0]
explod = []
for i in range(1,N+1):
    if mine[i-1] <= mine[i] >= mine[i+1]: explod.append(i)
for a in explod: print(a)