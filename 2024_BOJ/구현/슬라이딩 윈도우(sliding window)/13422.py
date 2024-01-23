#13422: 도둑
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N,M,K = map(int,input().split())
    money = list(map(int,input().split()))
    win = 0
    count = 0
    for i in range(M):
        win += money[i]
    if N==M and win < K:
        print(1)
        continue
    for i in range(N):
        if win < K:
            count += 1
        win += money[(i+M)%N]
        win -= money[i]
    print(count)