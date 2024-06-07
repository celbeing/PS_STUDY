#12899: 데이터 구조
import sys
input = sys.stdin.readline

def Insert(s,e,n,k):
    if s == e:
        tree[n] += 1
        return
    m = (s+e)//2
    if k>m:
        Insert(m+1,e,n*2+1,k)
    else:
        Insert(s,m,n*2,k)
    tree[n] += 1
    return

def Delete(s,e,n,k):
    if s == e:
        print(s)
        tree[n] -= 1
        return
    m = (s+e)//2
    if k > tree[n*2]:
        Delete(m+1,e,n*2+1,k-tree[n*2])
    else:
        Delete(s,m,n*2,k)
    tree[n] -= 1
    return

tree = [0]*(1<<22)
N = int(input())
for _ in range(N):
    S,X = map(int,input().split())
    if S == 1:
        Insert(1,2000000,1,X)
    else:
        Delete(1,2000000,1,X)