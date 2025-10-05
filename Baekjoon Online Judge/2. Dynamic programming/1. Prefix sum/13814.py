# 13814: Eleven Lover
import sys
input = sys.stdin.readline

while 1:
    seq = list(input().strip())
    if seq == ['0']: break
    count = [0] * 11
    verd = [0] * len(seq)
    verd[0] = int(seq[0])
    count[verd[0]] += 1
    for i in range(1, (len(seq))):
        p = int(seq[i])
        verd[i] = verd[i - 1]
        verd[i] += -p if i & 1 else p
        verd[i] %= 11
        count[verd[i]] += 1
    res = count[0]
    for i in range(len(seq) - 1):
        count[verd[i]] -= 1
        res += 0 if seq[i + 1] == '0' else count[verd[i]]
    print(res)