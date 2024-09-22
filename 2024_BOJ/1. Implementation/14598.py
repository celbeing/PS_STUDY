#14598: 인공지능 테트리스 (Small)
import sys
input = sys.stdin.readline
def score(board):
    ret = 0
    for i in range(20):
        for j in range(10):
            if board[i][j] == 0: break
        else:
            ret += 1
    return ret

def solution():
    st1 = [list(map(int, input().rstrip())) for _ in range(20)]
    st2 = []
    while st1:
        if st1[-1] == [0] * 10: st1.pop()
        else: st2.append(st1.pop())
    screen = []
    for i in range(20 - len(st2)): screen.append([0] * 10)
    while st2: screen.append(st2.pop())

    blocks = [[(0,0),(0,1),(1,0),(2,0)],
              [(0,0),(0,1),(0,2),(1,2)],
              [(0,1),(1,1),(2,0),(2,1)],
              [(0,0),(1,0),(1,1),(1,2)],
              [(0,0),(0,1),(1,1),(2,1)],
              [(0,2),(1,0),(1,1),(1,2)],
              [(0,0),(1,0),(2,0),(2,1)],
              [(0,0),(0,1),(0,2),(1,0)],
              [(0,0),(1,0),(2,0),(3,0)],
              [(0,0),(0,1),(0,2),(0,3)],
              [(0,0),(0,1),(1,0),(1,1)],
              [(0,0),(1,0),(1,1),(2,1)],
              [(0,1),(0,2),(1,0),(1,1)],
              [(0,0),(1,0),(1,1),(2,0)],
              [(0,0),(0,1),(0,2),(1,1)],
              [(0,1),(1,0),(1,1),(2,1)],
              [(0,1),(1,0),(1,1),(1,2)],
              [(0,1),(1,0),(1,1),(2,0)],
              [(0,0),(0,1),(1,1),(1,2)]]

    res = 0
    for b in blocks:
        pos = [list(b[i]) for i in range(4)]
        over = False
        for y in range(10):
            flag = False
            for x in range(21):
                pos_d = [pos[i][:] for i in range(4)]
                for i in range(4):
                    pos_d[i][0] += x
                    if pos_d[i][0] >= 20: flag = True
                    elif screen[pos_d[i][0]][pos_d[i][1]]: flag = True
                if flag:
                    for i in range(4):
                        pos_d[i][0] -= 1
                        screen[pos_d[i][0]][pos_d[i][1]] += 1
                    s = score(screen)
                    if res < s: res = s
                    for i in range(4):
                        screen[pos_d[i][0]][pos_d[i][1]] -= 1
                    break
            for i in range(4):
                pos[i][1] += 1
                if pos[i][1] == 10: over = True; break
            if over: break
    print(res)
solution()