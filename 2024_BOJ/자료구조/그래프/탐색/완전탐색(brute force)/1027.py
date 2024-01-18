#1027: 고층 건물
import sys
input = sys.stdin.readline
N = int(input())
building = list(map(int,input().split()))
peek = 0

for i in range(N):
    count = 0
    incleft = 1e9
    incright = -1e9
    for j in range(i-1,-1,-1):
        inclination = (building[i]-building[j])/(i-j)
        if inclination < incleft:
            incleft = inclination
            count += 1
    for j in range(i+1,N):
        inclination = (building[j]-building[i])/(j-i)
        if inclination > incright:
            incright = inclination
            count += 1
    if count > peek:
        peek = count

print(peek)