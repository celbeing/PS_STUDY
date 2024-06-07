#A: 가지 한 두름 주세요
import sys
input = sys.stdin.readline
ep = [list(input().split()) for _ in range(10)]
for i in range(10):
    for j in range(1,10):
        if ep[i][0] == ep[i][j]:
            continue
        else:
            break
    else:
        print(1)
        exit()
    for j in range(1,10):
        if ep[0][i] == ep[j][i]:
            continue
        else:
            break
    else:
        print(1)
        exit()

print(0)