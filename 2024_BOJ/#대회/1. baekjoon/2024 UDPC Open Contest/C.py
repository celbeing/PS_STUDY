#31714: 지정좌석 배치하기 1
import sys
input = sys.stdin.readline
N,M,D = map(int,input().split())
flag = True
seat = [sorted(list(map(int,input().split()))) for _ in range(N)]

for i in range(1,N):
    for j in range(M):
        if seat[i][j]+D <= seat[i-1][j]:
            flag = False
            break
    if not(flag): break

if flag: print("YES")
else: print("NO")