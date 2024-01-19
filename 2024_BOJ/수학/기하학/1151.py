#1151: 그림자
import sys
input = sys.stdin.readline

xyz = list(map(int,input().split()))
x,y,z = map(int,input().split())
X = [xyz[0],xyz[0],xyz[0],xyz[0],xyz[3],xyz[3],xyz[3],xyz[3]]
Y = [xyz[1],xyz[1],xyz[4],xyz[4],xyz[1],xyz[1],xyz[4],xyz[4]]
Z = [xyz[2],xyz[5],xyz[2],xyz[5],xyz[2],xyz[5],xyz[2],xyz[5]]
shade = []
for i in range(8):
    a,b,c = X[i],Y[i],Z[i]
    if c >= z: continue
    shade.append((x-(z*(x-a)/(z-c)), y-(z*(y-b)/(z-c))))
if len(shade) < 8:
    print(-1)
    exit()

def ccw(a, b, c):
    k = (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])
    if k > 0: return 1
    elif k < 0: return -1
    else: return 0