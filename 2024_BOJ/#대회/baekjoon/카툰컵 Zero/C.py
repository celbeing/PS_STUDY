#C: 생일 축하합니다~
import sys
input = sys.stdin.readline
N = int(input())
name = [input().rstrip() for _ in range(N)]
lied = False
for a in name:
    print('?',a,flush=True)
    i = int(input())
    print('?',a,flush=True)
    j = int(input())
    if 1 in [i,j]:
        print('!',a,flush=True)
        exit()