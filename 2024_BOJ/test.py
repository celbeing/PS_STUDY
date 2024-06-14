import sys
input = sys.stdin.readline
rate = list(map(int,input().split()))
r = [[0]*8 for _ in range(8)]
for i in range(1,8): r[0][i] = rate[i-1]/100
for i in range(2,8): r[1][i] = rate[i+5]/100
for i in range(3,8): r[2][i] = rate[i+10]/100
for i in range(4,8): r[3][i] = rate[i+14]/100
for i in range(5,8): r[4][i] = rate[i+17]/100
for i in range(6,8): r[5][i] = rate[i+19]/100
for i in range(7,8): r[6][i] = rate[i+20]/100
for i in range(1,8):
    for j in range(i):
        r[i][j] = 1-r[j][i]

f = [0]*8
for i in range(4):
    f[i*2] = r[i*2][i*2+1]
    f[i*2+1] = r[i*2+1][i*2]

for i in range(8):
    