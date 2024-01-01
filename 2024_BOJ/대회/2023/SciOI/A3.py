# 균형 잡힌 등급
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
scores = [list(map(int,input().split())) for _ in range(N)]
scores.sort()
stack = deque()
stack.append((scores[0][0],scores[0][1],1))

for i in range(1,N):
    if stack and scores[i][0] == stack[-1][0]:
        stack[-1][1] = scores[i][1]
        stack[-1][2]+=1
    elif not stack or scores[i][1] > stack[-1][1]:
        stack.append((scores[i][0],scores[i][1],1))
    else:
        count = 1
        high = scores[i][1]
        while stack and scores[i][1] <= stack[-1][1]:
            a,b,c = stack.pop()
            count += c
            if high < b:
                high = b
        stack.append((scores[i][0],high,count))

parts = [0]
for k in stack:
    parts.append(k[2])
del parts[0]
p = len(parts)
if p < 3:
    print(-1)
else:
    a,b,c = 1,0,p-2
    ga,gb,gc = parts[0],0,parts[-1]
    while a < c:
        ta = ga+parts[a]
        tc = gc+parts[c]
        if abs(ga-tc) < abs(ta-gc):
            c-=1
            gc=tc
            b=c
        else:
            a+=1
            ga=ta
            b=a
    gb = parts[b]
    u = max(ga,gb,gc)-min(ga,gb,gc)
    while 0<b<p-1:
        lb,ta,rb,tc = 0,0,0,0
        if b > 1:
            lb = gb+parts[b-1]
            ta = ga-parts[b-1]
        if b < p-1:
            rb = gb+parts[b+1]
            tc = gc-parts[b+1]

        ul,ur = 0,0

        if lb==rb==0:
            break
        elif lb > 0 and rb == 0:
            ul = max(ta,lb,gc)-min(ta,lb,gc)
            if u >= ul:
                b-=1
                gb = lb
                ga = ta
                u = ul
            else:
                break
        elif rb > 0 and lb == 0:
            ur = max(ga,rb,tc)-min(ga,rb,tc)
            if u >= ur:
                b+=1
                gb = rb
                gc = tc
                u = ur
            else:
                break
        else:
            if ul > ur:
                if u >= ur:
                    b+=1
                    gb = rb
                    gc = tc
                    u = ur
                else:
                    break
            else:
                if u >= ul:
                    b-=1
                    gb = lb
                    ga = ta
                    u = ul
                else:
                    break
    print(u)