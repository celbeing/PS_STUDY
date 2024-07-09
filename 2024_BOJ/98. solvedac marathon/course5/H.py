import sys
input = sys.stdin.readline
N,w = map(int,input().split())
B,S = [],[]
for _ in range(N):
    t,s = map(int,input().split())
    if t == 3: S.append(s)
    else: B.append(s)
B.sort(reverse=True)
S.sort(reverse=True)

for i in range(1,len(B)):
    B[i] += B[i-1]
for i in range(1,len(S)):
    S[i] += S[i-1]


si = min(len(S),w//3)
bi = min(len(B),(w-si*3)//5)

B.append(0)
S.append(0)
peek = S[si-1]+B[bi-1]
while si > 0 and bi < len(B):
    si -= 1
    if si*3+bi*5+5 <= w:
        bi += 1
    if peek < S[si-1]+B[bi-1]:
        peek = S[si-1]+B[bi-1]
print(peek)