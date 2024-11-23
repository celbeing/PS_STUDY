# 20055: 컨베이어 벨트 위의 로봇
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    N, K = map(int, input().split())
    dura = deque(list(map(int, input().split())))
    robo = deque([0] * (2 * N))

    def dura_check():
        broke = 0
        for i in range(N * 2):
            if dura[i] == 0: broke += 1
        return False if broke < K else True

    stage = 0
    while True:
        stage += 1
        dura.appendleft(dura.pop())
        robo.appendleft(robo.pop())
        if robo[N - 1]: robo[N - 1] = 0

        for i in range(N - 2, -1, -1):
            if robo[i]:
                if dura[i + 1] and robo[i + 1] == 0:
                    robo[i] -= 1
                    robo[i + 1] += 1
                    dura[i + 1] -= 1

        if dura[0]:
            robo[0] += 1
            dura[0] -= 1
        if robo[N - 1]: robo[N - 1] = 0
        if dura_check(): break
    print(stage)
solution()