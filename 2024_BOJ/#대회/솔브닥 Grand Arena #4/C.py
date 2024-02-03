#C번 - 아리스, 청소합니다!
import sys
input = sys.stdin.readline
H,W = map(int,input().split())
R,C,D = map(int,input().split())
d = [[-1,0],[0,1],[1,0],[0,-1]]
orderA = [list(map(int,input().rstrip())) for _ in range(H)]
orderB = [list(map(int,input().rstrip())) for _ in range(H)]
clean = [[0 for _ in range(W)] for _ in range(H)]
flag = False
last = [R,C,D]
moved = 0
count = 1

while True:
    if 0<=R<H and 0<=C<W:
        if clean[R][C] == 0:
            flag = True
            moved += count
            count = 1
            clean[R][C] = 1
            D += orderA[R][C]
            D %= 4
            R += d[D][0]
            C += d[D][1]
        else:
            if flag:
                last = [R,C,D]
                flag = False
            elif [R,C,D] == last:
                break
            D += orderB[R][C]
            D %= 4
            R += d[D][0]
            C += d[D][1]
            count += 1
    else:
        break
print(moved)