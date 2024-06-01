import sys
input = sys.stdin.readline
T = int(input())
a = [[0,1,2,3],[0,1,4,5],[4,5,6,7],[1,3,5,7],[0,2,4,6],[2,3,6,7]]
for _ in range(T):
    c = sorted(list(map(int,input().split())))
    if c in a: print("YES")
    else: print("NO")