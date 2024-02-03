#D번 - 반 나누기
import sys
input = sys.stdin.readline

def area(a,b,c):
    return abs((a[0]*b[1]+b[0]*c[1]+c[0]*a[1])-(a[1]*b[0]+b[1]*c[0]+c[1]*a[0]))/2

N = int(input())
S = [0]
point = list(map(int,input().split()))
p = [list(map(int,input().split()))]
for i in range(N-2):
    p.append(list(map(int,input().split())))
    S.append(area(point,p[i],p[i+1]) + S[i])
D = S[-1]/2

s = 0
while S[s] <= D:
    s += 1
K = S[s]-S[s-1]
R = (S[s]-D)/K
print("YES")
print("1 0")
print(*[s+1,1-R])