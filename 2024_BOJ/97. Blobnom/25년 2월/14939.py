# 14939: 불 끄기
import sys
input = sys.stdin.readline

bulb = [[0] * 10 for _ in range(10)]
for i in range(10):
    line = input().strip()
    for j in range(10):
        if line[j] == 'O':
            bulb[i][j] = 1

def switching():
    res = 101
    for i in range(1 << 10):
        now = [[0] * 10 for _ in range(10)]
        for j in range(10):
            for k in range(10):
                now[j][k] = bulb[j][k]
        count = 0
        switch = [[0] * 10 for _ in range(10)]
        d = 1000000000
        for j in range(10):
            if i & d:
                count += 1
                switch[0][j] = 1
            d >>= 1

        for j in range(1, 10):
            if bulb[j - 1][0] ^ switch[j - 1][0] ^ switch[j - 1][1]: