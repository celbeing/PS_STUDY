#25308: 방사형 그래프
import sys, itertools
input = sys.stdin.readline

def ccw(a, b, c):
    k = (a[1]-b[1])*(b[0]-c[0])-(a[0]-b[0])*(b[1]-c[1])
    if k > 0: return 1
    elif k < 0: return -1
    else: return 0

a = list(map(int,input().split()))
k = 0.70710678118654752440084436210485
order = [i for i in range(1,8)]
perm = itertools.permutations(order,7)
count = 0
for t in perm:
    p = [0] + list(t)
    for i in range(-2,6):
        x = (a[p[i]],0)
        y = (a[p[i+1]]*k,a[p[i+1]]*k)
        z = (0,a[p[i+2]])
        if ccw(x,y,z) <= 0:
            pass
        else:
            break
    else:
        count += 1
print(count*8)