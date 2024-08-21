#12993: 이동3
import sys
input = sys.stdin.readline
x,y = map(int,input().split())
while x > 0 or y > 0:
    if (x%3)+(y%3)==1:
        x //= 3
        y //= 3
    else:
        print(0)
        exit()
print(1)