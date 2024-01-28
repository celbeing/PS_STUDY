#A번 - 장난감 강아지
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
order = list(input().rstrip())
move = {"U":[-1,0],"D":[1,0],"L":[0,-1],"R":[0,1]}
track = [[0,0] for _ in range(N)]
track[0] = move[order[0]]
for i in range(1,N):
    track[i][0] = track[i-1][0] + move[order[i]][0]
    track[i][1] = track[i-1][1] + move[order[i]][1]
dx = -track[-1][0]
dy = -track[-1][1]
flag = False
if dx * dy != 0:
    for k in track:
        if k[0] % dx == 0 and k[1] % dy == 0:
            if k[0] // dx == k[1] // dy:
                if 0 <= k[0] // dx < K:
                    flag = True
                    break
elif dx == dy:
    flag = True
elif dx == 0:
    for k in track:
        if k[0] == 0 and k[1] % dy == 0:
            if 0 <= k[1] // dy < K:
                flag = True
                break
else:
    for k in track:
        if k[1] == 0 and k[0] % dx == 0:
            if 0 <= k[0] // dx < K:
                flag = True
                break

if flag:
    print("YES")
else:
    print("NO")
