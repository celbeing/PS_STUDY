#D: 장난을 잘 치는 토카 양
import sys
input = sys.stdin.readline
A,B = map(int,input().split())
C,D = map(int,input().split())
K = int(input())

t,reach = 0,0
if K == 0:
    t = A//B
    if A%B > 0:
        t += 1
    if D*t >= A+C:
        print(-1)
    else:
        print(t)
    exit()

t = B//K
reach = B*t-K*t*(t-1)//2+B%K
if reach < A:
    print(-1)
    exit()

s,e = 0,t
if B%K>0:
    e += 1

while s < e:
    m = (s+e)//2
    new_reach = B*m-K*m*(m-1)//2

    if new_reach > A:
        e = m
    elif new_reach < A:
        s = m+1
    else:
        s = m
        break

if D*s >= A+C:
    print(-1)
else:
    print(s)