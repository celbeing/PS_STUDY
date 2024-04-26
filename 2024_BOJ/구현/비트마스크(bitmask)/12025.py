# 12025: 장난꾸러기 영훈
import sys
input = sys.stdin.readline

change = {1:6,2:7}
p = list(map(int,input().rstrip()))
k = int(input())
check = []
for d in range(len(p)):
    if p[d] in [1,2,6,7]:
        check.append(d)
        if p[d] == 6: p[d] = 1
        elif p[d] == 7: p[d] = 2
check.reverse()
l = 1<<len(check)
if k > l or k < 1: print(-1)
else:
    k-=1
    for i in range(len(check)):
        if k & 1<<i:
            p[check[i]] = change[p[check[i]]]
    print(*p,sep="")