# 12787: 지금 밥이 문제냐
import sys
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        m, n = map(str, input().split())
        if m == '1':
            res = 0
            ip = list(map(int, n.split('.')))
            for k in ip:
                res <<= 8
                res += k
            print(res)
        else:
            ip = []
            n = int(n)
            for i in range(8):
                ip.append(str(n & 255))
                n >>= 8
            ip.reverse()
            print('.'.join(ip))
solution()