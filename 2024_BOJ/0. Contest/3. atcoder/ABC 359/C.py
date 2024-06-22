import sys
input = sys.stdin.readline
sx,sy = map(int,input().split())
tx,ty = map(int,input().split())
x = 0
y = abs(sy-ty)

s = sx+sy
t = tx+ty
if sx < tx:
    if s&1:
        if t&1:
            x = tx-sx-1
        else:
            x = tx-sx
    else:
        if t&1:
            x = tx-sx-2
        else:
            x = tx-sx-1
else:
    if s&1:
        if t&1:
            x = sx-tx-1
        else:
            x = sx-tx-2
    else:
        if t&1:
            x = sx-tx
        else:
            x = sx-tx-1

result = y
if x > y:
    result += (x-y+1)//2
print(result)