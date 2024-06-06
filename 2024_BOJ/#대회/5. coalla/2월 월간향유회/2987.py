#2987: 사과나무
import sys
input = sys.stdin.readline

def ccw(a,b,c):
    k = (a[1]-b[1])*(b[0]-c[0])-(a[0]-b[0])*(b[1]-c[1])
    if k > 0: return 3
    elif k < 0: return 1
    else: return 0

A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))
C = tuple(map(int,input().split()))
area = abs(A[0]*B[1]+B[0]*C[1]+C[0]*A[1]-A[1]*B[0]-B[1]*C[0]-C[1]*A[0])/2
print("{:.1f}".format(area))

count = 0
N = int(input())
for _ in range(N):
    t = tuple(map(int,input().split()))
    s = ccw(A,B,t) + ccw(B,C,t) + ccw(C,A,t)
    if s == 4 or s == 5 or s == 7: continue
    count += 1
print(count)