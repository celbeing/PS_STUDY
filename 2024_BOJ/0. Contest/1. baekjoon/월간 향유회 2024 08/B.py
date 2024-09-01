import sys
input = sys.stdin.readline
l = set()
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if a in l or b in l or c in l:
        print(1)
        exit()
    else:
        l.update([a,b,c])
print(0)