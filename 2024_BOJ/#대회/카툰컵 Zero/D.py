#D: 장난을 잘 치는 토카 양
import sys
input = sys.stdin.readline
A,B = map(int,input().split())
C,D = map(int,input().split())
K = int(input())

t = B // K
dist = B*t-(t*(t-1)//2*K)+B%K
if dist < A:
    print(-1)
    exit()
elif dist == A:
    if D*(t+1) >= A+C:
        print(-1)
        exit()
dist -= B%K
if dist <= A:
    if D*(t+1) >= A+C:
        print(-1)
        exit()

d = (A+C)//D
s,e = 0,t
while s < e:
    m = (s+e)//2
    new_dist = B*m-(m*(m-1)//2*K)
    if new_dist > A:
        e = m-1
    elif new_dist < A:
        s = m+1
    else:
        s = m
        break
dist = B*s-(s*(s-1)//2*K)
if dist > A:
    s -= 1

tok_last = A-B*s-(s*(s-1)//2*K)
dol_last = A+C-(D*s)
if tok_last >= dol_last:
    print(-1)
    exit()

if tok_last > 0:
    tok_last -= B-K*s
    dol_last -= D
    s += 1
    if tok_last < 0: tok_last = 0
    if dol_last < 0: dol_last = 0
else:
    if dol_last <= 0:
        print(-1)
        exit()

if tok_last >= dol_last:
    print(-1)
    exit()
print(s)