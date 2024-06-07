#10997: 별 찍기 - 22
N = int(input())
if N == 1:
    print('*')
    exit()
d = [[0,-1],[1,0],[0,1],[-1,0]]
w,h = N*4-3,N*4-1
star = [['*' for _ in range(w)] for _ in range(h)]
x,y = 1,w-1
k = 0
while not(x == h//2 and y == w//2+1):
    star[x][y] = ' '
    x2,y2 = x+d[k][0]*2,y+d[k][1]*2
    if 0<=x2<h and 0<=y2<w and star[x2][y2] == '*':
        x += d[k][0]
        y += d[k][1]
    else:
        k = (k+1)%4
        x += d[k][0]
        y += d[k][1]
star[x][y] = ' '
for a in star:
    print(str(''.join(a)).rstrip())