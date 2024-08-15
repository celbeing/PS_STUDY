#27986: 평범한 구성적 문제
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
twin = [tuple(map(int,input().split())) for _ in range(M)]
twin.sort(key = lambda x: x[1]-x[0])
K = twin[0][1]-twin[0][0]+1
res = [(i%K)+1 for i in range(N)]
print(*res)