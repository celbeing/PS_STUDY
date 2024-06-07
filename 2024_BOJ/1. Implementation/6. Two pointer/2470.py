#2470: 두 용액
import sys,math
input = sys.stdin.readline
N = int(input())
liquid = sorted(list(map(int,input().split())))
l,r,result = 0,N-1,2e9
mem = [0,0]

while l < r:
    current = liquid[l] + liquid[r]
    if abs(current) < abs(result):
        mem[0] = liquid[l]
        mem[1] = liquid[r]
        result = current

    if current > 0:
        r-=1
    elif current < 0:
        l+=1
    else:
        break
print(*mem)