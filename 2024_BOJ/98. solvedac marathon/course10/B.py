#1064: 평행사변형
d = tuple(map(int,input().split()))
def ccw (a,b,c):
    k = (a[0]-b[0])*(b[1]-c[1])-(a[1]-b[1])*(b[0]-c[0])
    if k == 0: return 0
    else: return 1
def dist(a,b):
    return((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
a = dist((d[0],d[1]),(d[2],d[3]))
b = dist((d[2],d[3]),(d[4],d[5]))
c = dist((d[4],d[5]),(d[0],d[1]))
if ccw((d[0],d[1]),(d[2],d[3]),(d[4],d[5])): print(max(max(abs(a-b),abs(b-c)),abs(c-a))*2)
else: print(-1)