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

#8강
f = [0]*8
for i in range(4):
    f[i*2] = r[i*2][i*2+1]
    f[i*2+1] = r[i*2+1][i*2]

#4강
g = [0]*8
g[0] = f[0]*(f[2]*r[0][2]+f[3]*r[0][3])
g[1] = f[1]*(f[2]*r[1][2]+f[3]*r[1][3])

g[2] = f[2]*(f[0]*r[2][0]+f[1]*r[2][1])
g[3] = f[3]*(f[0]*r[3][0]+f[1]*r[3][1])

g[4] = f[4]*(f[6]*r[4][6]+f[7]*r[4][7])
g[5] = f[5]*(f[6]*r[5][6]+f[7]*r[5][7])

g[6] = f[6]*(f[4]*r[6][4]+f[5]*r[6][5])
g[7] = f[7]*(f[4]*r[7][4]+f[5]*r[7][5])

#준결
for i in range(4):
    f[i] = g[i]*(g[4]*r[i][4]+g[5]*r[i][5]+g[6]*r[i][6]+g[7]*r[i][7])
    f[i+4] = g[i+4]*(g[0]*r[i+4][0]+g[1]*r[i+4][1]+g[2]*r[i+4][2]+g[3]*r[i+4][3])

print(*f)