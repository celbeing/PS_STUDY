import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N,S,E = map(int,input().split())
    cost = 2
    if S == 1 or S == N:
        cost -= 1
        if E == 1 or E == N:
            cost -= 1
    elif abs(S-E) == 1:
        cost -= 1
    print(cost)