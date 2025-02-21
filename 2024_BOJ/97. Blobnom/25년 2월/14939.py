# 14939: 불 끄기
import sys
input = sys.stdin.readline

bulb = [[0] * 10 for _ in range(10)]
for i in range(10):
    line = input().strip()
    for j in range(10):
        if line[j] == 'O':
            bulb[i][j] = 1

def switching(act, state, d, count):
    if d == 10:
        # 남은 칸 조작
        return count

    next_state = [0] * d
    next_act = [0] * d

    next_state[0] = bulb[d - 1][0] ^ act[0]
    next_state[-1] = bulb[0][d - 1] ^ act[-1]
    for i in range(1, d - 1):
        next_state[i] = bulb[d - 1 - i][i] ^ act[i] ^ act[i - 1]

    for i in range(1, d):
        next_act[i] = state[i - 1] ^ next_act[i - 1]
    ret = switching(next_act, next_state, d + 1, count + sum(next_act))

    for i in range(d):
        next_act[i] ^= 1
        next_state[i] ^= 1
    ret = max(ret, switching(next_act, d + 1, count + sum(next_act)))

    return ret

switching([], [], 1, 0)