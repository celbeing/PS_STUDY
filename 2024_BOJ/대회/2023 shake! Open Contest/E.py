#E: 마카롱카마
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
red = list(map(int,input().rstirp()))
blue = [0]*N
coque = []
for i in range(N):
    coque.append((red[i],i))
coque.sort()
count = [0]*10
for i in range(N):
    count[coque[i]]+=1
check = [0]*N
for a, index in coque:
    if check[index] == 1:
        continue
    if blue[index] == 0:
        if red[index] != red[N-index-1]:
            blue[N-index-1] = a
            count[a] -= 1
        else:
            for i in range(0,N):
                if blue[i] == blue[N-i-1] == 0:
                    blue[i] = a
                    blue[N-i-1] = a
                    check[N-i-1] = 1
                    count[a] -= 2
    else:
        i = 0
