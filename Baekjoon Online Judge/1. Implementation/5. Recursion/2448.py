#2448: 별 찍기 - 11
N = int(input())
map = [[' ' for _ in range(N*2-1)] for _ in range(N)]
x = [0, 1, 1, 2, 2, 2, 2, 2]
y = [2, 1, 3, 0, 1, 2, 3, 4]
def star(p, map, a, b):
    if p == 3:
        for i in range(8):
            map[a + x[i]][b + y[i]] = '*'
    else:
        q = p // 2
        star(q,map,a+q,b)
        star(q,map,a,b+q)
        star(q,map,a+q,b+q+q)

star(N,map,0,0)
for i in range(N):
    print(''.join(map[i]))