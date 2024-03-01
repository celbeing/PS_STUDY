#A: 소수가 아닌 수 3
import sys
input = sys.stdin.readline
N = int(input())
if N == 0:
    print("NO")
    exit()
d = sorted(list(map(int,input().split())))
if d[-1] == 0:
    print("YES")
    print(0)
else:
    print("YES")
    print("{}{}{}".format(d[-1],d[-1],d[-1]))