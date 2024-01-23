#10833: 사과
import sys
input = sys.stdin.readline
N = int(input())
apple = 0
for i in range(N):
    s,a = map(int,input().split())
    while s <= a:
        a -= s
    apple += a
print(apple)