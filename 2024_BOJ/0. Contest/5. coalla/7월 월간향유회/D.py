#2527: 직사각형
import sys
input = sys.stdin.readline

def judge(d):
    area = max(min(d[2],d[6])-max(d[0],d[4]),0)*max(min(d[3],d[7])-max(d[1],d[5]),0)
    if area > 0: return "a"
    else:
        if d[0] == d[6] or d[2] == d[4]:
            if d[1]<d[7]<=d[3] or d[1]<=d[5]<d[3]: return "b"
            elif d[7] == d[1] or d[5] == d[3]: return "c"
        elif d[1] == d[7] or d[3] == d[5]:
            if d[0]<d[6]<=d[2] or d[0]<=d[4]<d[2]: return "b"
            elif d[6] == d[0] or d[4] == d[2]: return "c"
    return "d"

for _ in range(4):
    print(judge(tuple(map(int,input().split()))))