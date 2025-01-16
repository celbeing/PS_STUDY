# 1529: 동민 수열
import sys
input = sys.stdin.readline
def solution():
    n, l = map(int, input().split())
    arr = list(map(str, input().split()))
    div = 1234567891

    gm_number = [0] * 4
    check = set()
    for a in arr:
        if a in check: continue
        for b in a:
            if not(b == '4' or b == '7'):
                break
        else:
            if a[0] == '4':
                if a[-1] == '4':
                    gm_number[0] += 1
                else:
                    gm_number[1] += 1
            else:
                if a[-1] == '4':
                    gm_number[2] += 1
                else:
                    gm_number[3] += 1
            check.add(a)

    def mat_mult(mat, rix):
        m1 = (mat[0]+mat[3])*(rix[0]+rix[3])
        m2 = (mat[1]+mat[3])*rix[0]
        m3 = mat[0]*(rix[2]-rix[3])
        m4 = mat[3]*(rix[1]-rix[0])
        m5 = (mat[0]+mat[2])*rix[3]
        m6 = (mat[1]-mat[0])*(rix[0]+rix[2])
        m7 = (mat[2]-mat[3])*(rix[1]+rix[3])
        return [(m1+m4-m5+m7)%div, (m2+m4)%div, (m3+m5)%div, (m1-m2+m3+m6)%div]

    def fast_power(mat, k):
        if k == 0:
            return [1,0,0,1]
        elif k == 1:
            return mat
        mul = fast_power(mat, k >> 1)
        if k & 1:
            return mat_mult(mat_mult(mul, mul), mat)
        else:
            return mat_mult(mul, mul)

    mat = fast_power(gm_number, l - 1)
    res = mat[0] * (gm_number[0] + gm_number[2]) + mat[2] * (gm_number[1] + gm_number[3])
    res += mat[1] * (gm_number[0] + gm_number[2]) + mat[3] * (gm_number[1] + gm_number[3])
    print(res % div)
solution()