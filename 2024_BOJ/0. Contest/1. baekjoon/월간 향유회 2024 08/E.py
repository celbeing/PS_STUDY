import sys
input = sys.stdin.readline
for _ in range(int(input())):
    k = list(map(int,input().split()))
    if sum(k)%2 == 0:
        print("YES")
    else:
        print("NO")