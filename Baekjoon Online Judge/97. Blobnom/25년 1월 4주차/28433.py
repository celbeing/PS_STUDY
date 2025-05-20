# 28433: 게리맨더링
import sys
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        res = 0
        prefix = 0
        for k in a:
            if k > 0:
                if prefix + k > 0:
                    if prefix > 0:
                        res += 1
                        prefix = k
                    else:
                        prefix += k
                else:
                    res -= 1
                    prefix = k
            elif k < 0:
                if prefix + k > 0:
                    prefix += k
                else:
                    if prefix <= 0:
                        prefix += k
                    else:
                        res += 1
                        prefix = k
        res += 1 if prefix > 0 else -1

        print('YES' if res > 0 else 'NO')
solution()