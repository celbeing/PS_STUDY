import sys
input = sys.stdin.readline
for _ in range(int(input())):
    d = list(map(int,input().split()))
    sw = (d[2]-d[0])*(d[3]-d[1])
    dp = (max(min(d[2],d[6])-max(d[0],d[4]),0))*(max(min(d[3],d[7])-max(d[1],d[5]),0))
    print(sw-dp)