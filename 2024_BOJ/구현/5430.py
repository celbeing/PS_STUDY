#5430: AC
import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    R = False
    l, r = 0, 0
    p = list(input().rstrip())
    n = int(input())
    x = []
    if n > 0:
        x = list(map(int,input().strip('[]\n').split(',')))
    else:
        input()
    recent = -1
    for i in range(len(p)):
        if p[i] == 'R':
            R = not R
        elif R:
            r+=1
        else:
            l+=1
    if r+l > n:
        print("error")
    else:
        if r > 0:
            result = x[l:-r]
        else:
            result = x[l:]
        if R:
            result.reverse()
        print('[',end='')
        for i in range(len(result)-1):
            print(result[i],end='')
            print(',',end='')
        if result:
            print(result[-1],end='')
        print(']')