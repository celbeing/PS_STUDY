# 29874: Põranda katmine
import sys
input = sys.stdin.readline
def solution():
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    p1 = [(a, b), (b, a)]
    p2 = [(c, d), (d, c)]
    if (x, y) in p1:
        print(0,0,x,y)
        print('Z')
        return
    elif (x, y) in p2:
        print('Z')
        print(0,0,x,y)
        return
    else:
        for P1 in p1:
            for P2 in p2:
                if P1[0] == P2[0] == x and P1[1] <= y >= P2[1] and P1[1] >= y - P2[1]:
                    print(0,0,P1[0],P1[1])
                    print(0,y-P2[1],x,y)
                    return
                elif P1[1] == P2[1] == y and P1[0] <= x >= P2[0] and P1[0] >= x - P2[0]:
                    print(0,0,P1[0],P1[1])
                    print(x-P2[0],0,x,y)
                    return
    print('EI SAA')
solution()