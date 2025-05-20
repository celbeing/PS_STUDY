#17219: 비밀번호 찾기
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
pw = dict()
for _ in range(N):
    n,p = map(str,input().split())
    pw[n] = p
for _ in range(M):
    print(pw[input().rstrip()])