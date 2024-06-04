# K: 시소 배열
import sys
input = sys.stdin.readline
Q = int(input())
arr = [0]*500001
pre = [0]*500001
s,e = 0,1
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        arr[e] = q[1]
        pre[e] = pre[e-1]+q[1]
        e+=1
    else:
        m = (s+e-1)//2
        f = pre[m]-pre[s]
        b = pre[e-1]-pre[m]
        if f <= b:
            print(f)
            s = m
        else:
            print(b)
            e = m+1
print(*arr[s+1:e])