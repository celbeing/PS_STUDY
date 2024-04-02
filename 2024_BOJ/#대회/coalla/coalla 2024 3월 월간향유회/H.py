#7795: 먹을 것인가 먹힐 것인가
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = sorted(list(map(int,input().split())))
    B.append(A[-1]+1)
    count = 0
    point = 0
    for i in range(N):
        while A[i] > B[point]:
            point += 1
        count += point
    print(count)