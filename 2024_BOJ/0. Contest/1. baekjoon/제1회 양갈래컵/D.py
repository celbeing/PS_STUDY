#D: 양갈래 배열 출력하기
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
d = [(0,1),(1,0),(0,-1),(-1,0)]
di = 0
array = [[0 for _ in range(M)] for _ in range(N)]
way = input().rstrip()
x,y = 0,0
if way == "U" or way == "D":
    di = 2
    x,y = N-1,M//2-1
    for i in range(N):
        array[i][M//2] = i+1
    k = N+1
    while k <= N*(M//2+1):
        array[x][y] = k
        array[x][M-y-1] = k
        if 0 <= x+d[di][0] < N and 0 <= y+d[di][1] < M//2:
            if array[x+d[di][0]][y+d[di][1]] == 0:
                pass
            else:
                di += 1
        else:
            di += 1
        di %= 4
        x += d[di][0]
        y += d[di][1]
        k += 1
    if way == "U":
        for a in array:
            print(*a)
    else:
        for a in reversed(array):
            print(*a)

else:
    di = 1
    x,y = N//2+1,M-1
    for i in range(M):
        array[N//2][i] = i+1
    k = M+1
    while k <= (N//2+1)*M:
        array[x][y] = k
        array[N-x-1][y] = k
        if 0 <= x+d[di][0] < N and 0 <= y+d[di][1] < M:
            if array[x+d[di][0]][y+d[di][1]] == 0:
                pass
            else:
                di += 1
        else:
            di += 1
        di %= 4
        x += d[di][0]
        y += d[di][1]
        k += 1
    if way == "L":
        for a in array:
            print(*a)
    else:
        for a in array:
            print(*reversed(a))