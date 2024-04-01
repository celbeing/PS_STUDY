#11688: 최소공배수 찾기
import sys,math
input = sys.stdin.readline
a,b,L = map(int,input().split())

dL = []
for i in range(1,int(L**0.5)+1):
    if ~(L%i):
        dL.append(i)
        dL.append(L//i)
dL.sort()

l = math.lcm(a,b)
if l==L:
    print(1)
elif L%l:
    print(-1)
else:
    for d in dL:
        if math.lcm(l,d)==L:
            print(d)
            exit()