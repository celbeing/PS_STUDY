#10993: 별 찍기 - 18
n = int(input())
h,w = 1,1
for i in range(n-1):
    h = h*2+1
    w = w*2+3
star = []
a,b = 0,0
if n % 2 == 1:
    for i in range(h):
        star.append([' ' for _ in range(h+i)])
    a,b = 0,h-1
else:
    for i in range(h):
        star.append([' ' for _ in range(w-i)])
    a,b = h-1,h-1

for i in range(n):
    if (n-i) % 2 == 1:
        for k in range(h-1):
            star[a+k][b+k] = '*'
            star[a+k][b-k] = '*'
        for k in range(b-h+1,b+h):
            star[a+h-1][k] = '*'
        a += h-2
    else:
        for k in range(h-1):
            star[a-k][b+k] = '*'
            star[a-k][b-k] = '*'
        for k in range(b-h+1,b+h):
            star[a-h+1][k] = '*'
        a += 2-h
    h //= 2

for k in star:
    print(''.join(k))