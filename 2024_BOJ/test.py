import sys
input = sys.stdin.readline
N = int(input())
D,P = 0,0
for _ in range(N):
    if input().rstrip() == "D": D += 1
    else: P += 1
    if D-P==2 or P-D==2: break
print("{}:{}".format(D,P))