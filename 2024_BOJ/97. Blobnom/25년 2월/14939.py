# 14939: 불 끄기
import sys
input = sys.stdin.readline

bulb = [[0] * 12 for _ in range(12)]
for i in range(1, 11):
    line = input().strip()
    for j in range(10):
        if line[j] == 'O':
            bulb[i][j + 1] = 1

def switching():
    res = 101
    for b in range(1 << 10):
        switch = [[0] * 12 for _ in range(12)]
        d = 1 << 9
        count = 0
        for i in range(1, 11):
            if b & d:
                switch[1][i] = 1
                count += 1
            d >>= 1
        for i in range(2, 10):
            for j in range(1, 11):
                if bulb[i - 1][j] ^ switch[i - 1][j - 1] ^ switch[i - 1][j] ^ switch[i - 1][j + 1] ^ switch[i - 2][j]:
                    count += 1
                    switch[i][j] = 1
                if count >= res: break
            if count >= res: break
        if count >= res: continue
        if bulb[9][1] ^ switch[9][1] ^ switch[9][2] ^ switch[8][1]:
            count += 1
            switch[10][1] = 1
        for j in range(2, 11):
            if bulb[9][j] ^ switch[9][j - 1] ^ switch[9][j] ^ switch[9][j + 1] ^ switch[8][j]:
                count += 1
                switch[10][j] = 1
            if bulb[10][j - 1] ^ switch[9][j - 1] ^ switch[10][j - 1] ^ switch[10][j] ^ switch[10][j - 2]:
                count = 101
                break
        if bulb[10][10] ^ switch[10][9] ^ switch[9][10] ^ switch[10][10]:
            continue
        if res > count:
            res = count
    print(res if res <= 100 else -1)
switching()