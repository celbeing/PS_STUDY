#2493: 탑
import sys
input = sys.stdin.readline
N = int(input())
tower = list(map(int,input().split()))
tower.insert(0,0)
recieve = [0]*(N+1)
sign = []
for i in range(N,0,-1):
    if len(sign) == 0:
        sign.append(i)
    else:
        while len(sign) > 0 and tower[sign[-1]] < tower[i]:
            recieve[sign.pop()] = i
        sign.append(i)
print(*recieve[1:])