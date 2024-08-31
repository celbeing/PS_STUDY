import sys
input = sys.stdin.readline
L,R = 0,0
pr = 0
for _ in range(int(input())):
    a,s = map(str,input().split())
    if s == "L":
        if L:
            pr += abs(int(a)-L)
        L = int(a)
    else:
        if R:
            pr += abs(int(a)-R)
        R = int(a)
print(pr)