#1028: 다이아몬드 광산
import sys
input = sys.stdin.readline
R,C = map(int,input().split())
mine = [list(map(int,input().rstrip())) for _ in range(R)]
lu = [[0 for _ in range(C+2)] for _ in range(R+2)]
ru = [[0 for _ in range(C+2)] for _ in range(R+2)]
ld = [[0 for _ in range(C+2)] for _ in range(R+2)]
rd = [[0 for _ in range(C+2)] for _ in range(R+2)]

for i in range(1,R+1):
    for j in range(1,C+1):
        if mine[i-1][j-1] == 1:
            lu[i][j] = lu[i-1][j-1]+1
            ru[i][j] = ru[i-1][j+1]+1
for i in range(R,0,-1):
    for j in range(1,C+1):
        if mine[i-1][j-1] == 1:
            ld[i][j] = ld[i+1][j-1]+1
            rd[i][j] = rd[i+1][j+1]+1

peek = 0

for i in range(1,R+1):
    for j in range(1,C+1):
        poss = min(ld[i][j], rd[i][j])
        for k in range(poss):
            if i+k*2 > R: continue
            if min(lu[i+k*2][j], ru[i+k*2][j]) >= k+1:
                if peek < k+1:
                    peek = k+1

print(peek)