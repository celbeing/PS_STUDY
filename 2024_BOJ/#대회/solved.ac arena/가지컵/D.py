#D: :right plant:
import sys
input = sys.stdin.readline
N = int(input())
left = []
right = [1]
lsum = 0
rsum = 1
lcnt = 0
rcnt = 1

for i in range(2,N+1):
    if lsum+1 <= rsum:
        left.append(0)
        lcnt += 1
    else:
        right.append(0)
        rcnt += 1
    for j in range(lcnt):
        left[j]+=1
    for j in range(rcnt):
        right[j]+=1
    lsum += lcnt
    rsum += rcnt
right.sort()
print(*(left+right))