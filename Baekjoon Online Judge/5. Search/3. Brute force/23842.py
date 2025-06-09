# 23842: 성냥개비
import sys
input = sys.stdin.readline
n = int(input()) - 4
digit = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

def match_count(a, b, c):
    ret = digit[a % 10] + digit[b % 10] + digit[c % 10]
    ret += digit[a // 10] + digit[b // 10] + digit[c // 10]
    return ret

for a in range(0, 100):
    for b in range(0, 100 - a):
        if match_count(a, b, a+b) == n:
            print(f'{a:0>2}+{b:0>2}={a+b:0>2}')
            exit()
print('impossible')