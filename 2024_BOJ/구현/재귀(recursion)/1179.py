#1179: 마지막 요세푸스 문제
import sys
sys.setrecursionlimit(10**6)
N,K = map(int,input().split())

def josep(n,k):
    if n == 1:
        return 0
    if k == 1:
        return n-1
    if k > n:
        return (josep(n-1,k)+k)%n
    cnt = n//k
    res = josep(n-cnt,k)
    res -= n%k
    if res<0:
        res += n
    else:
        res += res//(k-1)
    return res

print(josep(N,K)+1)