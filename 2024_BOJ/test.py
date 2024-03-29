import sys
input = sys.stdin.readline
while True:
    d = list(input().split())
    if d[0] == '#': break
    age = int(d[1])
    weight = int(d[2])
    if age > 17 or weight >= 80:
        print(d[0],"Senior")
    else:
        print(d[0],"Junior")