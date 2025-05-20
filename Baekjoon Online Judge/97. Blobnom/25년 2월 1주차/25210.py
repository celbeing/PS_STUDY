# 25210: 정사각형 세기
import sys
input = sys.stdin.readline
def solution():
    cor = [tuple(map(int, input().split())) for _ in range(4)]
    ll = max(cor[1][2], cor[2][2])
    lr = min(cor[1][0], cor[2][0])
    rl = max(cor[0][0], cor[3][0])
    rr = min(cor[0][2], cor[3][2])
    dd = max(cor[2][3], cor[3][3])
    du = min(cor[2][1], cor[3][1])
    ud = max(cor[0][1], cor[1][1])
    uu = min(cor[0][3], cor[1][3])

    short = max(rl - lr, ud - du)
    long = min(rr - ll, uu - dd)

    count = 0
    for k in range(short, long + 1):
        l, r, d, u = 0, 0, 0, 0
        if ll + k < rl: l = rl - k
        else: l = ll
        if rr - k > lr: r = lr + k
        else: r = rr
        if dd + k < ud: d = ud - k
        else: d = dd
        if uu - k > du: u = du + k
        else: u = uu
        h, v = r - l + 1 - k, u - d + 1 - k
        if h > 0 and v > 0: count += h * v

    print(count)
solution()