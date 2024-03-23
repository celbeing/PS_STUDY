#1168: 요세푸스 문제 2
import sys,math
input = sys.stdin.readline
N,K = map(int,input().split())
h = math.ceil(math.log2(N))+1
seg = [0]*(1<<h)
arr = []

def segment(t,s,e,n):
    if s == e:
        t[n] = 1
        return t[n]
    m = (s+e)//2
    t[n] = segment(t,s,m,n*2)+segment(t,m+1,e,n*2+1)
    return t[n]

def josep(s,e,n,k):
    if s == e:
        seg[n] = 0
        arr.append(str(s))
        return
    m = (s+e)//2
    if k > seg[n*2]:
        josep(m+1,e,n*2+1,k-seg[n*2])
    else:
        josep(s,m,n*2,k)
    seg[n] -= 1
    return

segment(seg,1,N,1)

order = 0
for _ in range(N):
    order += K - 1
    order %= seg[1]
    order += 1
    josep(1,N,1,order)
    order -= 1
print("<",", ".join(arr),">",sep='')