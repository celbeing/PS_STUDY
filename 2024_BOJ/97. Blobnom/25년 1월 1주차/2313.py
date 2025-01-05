# 2313: 보석 구매하기
import sys
input = sys.stdin.readline
def solution():
    price = 0
    res = []
    for _ in range(int(input())):
        l = int(input())
        v = list(map(int, input().split()))
        a, b = 0, 0
        x, y = 0, 0
        high = v[0]
        sum = v[0]
        for i in range(1, l):
            if v[i] > 0:
                if sum <= 0:
                    sum = 0
                    x, y = i, i
                sum += v[i]
                y = i
                if sum > high:
                    a, b = x, y
                    high = sum
                elif sum == high:
                    if b - a > y - x:
                        a, b = x, y
            elif sum + v[i] > min(high, 0):
                sum += v[i]
            else:
                sum = v[i]
                x, y = i, i
                if sum > high:
                    high = sum
                    a, b = x, y
        res.append((a, b))
        price += high
    print(price)
    for a, b in res:
        print(a + 1, b + 1)
solution()