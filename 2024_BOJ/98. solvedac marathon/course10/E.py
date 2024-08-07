#25345: 루나의 게임 세팅
import sys, math
input = sys.stdin.readline
N,K = map(int,input().split())
A = list(map(int,input().split()))
print(math.comb(N,K)*(1<<K-1)%int(1e9+7))