#E: 가지 오이 당근
import sys
input = sys.stdin.readline
from collections import deque
T = int(input())

for _ in range(T):
    N = int(input())
    pick = list(input().rstrip())
    rslt = list(input().rstrip())
    win,lose,draw,G,D,O,Q = 0,0,0,0,0,0,0
    q = deque()
    wstnd,lstnd = -1,-1
    winner = ''
    loser = ''

    for i in range(N):
        if rslt[i] == 'D': draw+=1
        elif rslt[i] == 'W':
            win+=1
            if pick[i] != '?':
                wstnd = i
                winner = pick[i]
        else:
            lose+=1
            if pick[i] != '?':
                lstnd = i
                loser = pick[i]
        if pick[i] == 'G': G+=1
        elif pick[i] == 'D': D+=1
        elif pick[i] == 'O': O+=1
        else: q.append(i)
    Q = len(q)

    if 0<draw<N or (draw == 0 and D>0 and G>0 and O>0):
        print("NO")
        continue

    if draw == N:
        if N == 2:
            print("NO")
            continue

        if (G == 0 and D>0 and O>0) or (G>0 and D == O == 0):
            while q:
                pick[q.popleft()] = 'G'
            G += Q

        elif (D == 0 and G>0 and O>0) or (D>0 and G == O == 0):
            while q:
                pick[q.popleft()] = 'D'
            D += Q

        elif (O == 0 and G>0 and D>0) or (O>0 and G == D == 0):
            while q:
                pick[q.popleft()] = 'O'
            O += Q

        elif (G == 0 and D == 0 and O == 0) and Q == N:
            while q:
                pick[q.popleft()] = 'G'
            G += Q

        if G+D+O != N:
            print("NO")
            continue
        else:
            print("YES")
            print(''.join(pick))

    else:
        if win == 0 and lose == 0:
            print("NO")
            continue
        if win == N or lose == N:
            print("NO")
            continue

        if wstnd>=0:
            if winner == 'G': loser = 'O'
            elif winner == 'O': loser = 'D'
            else: loser = 'G'
        elif lstnd>=0:
            if loser == 'G': winner = 'D'
            elif loser == 'D': winner = 'O'
            else: winner = 'G'
        else:
            winner = 'G'
            loser = 'O'

        while q:
            k = q.popleft()
            if rslt[k] == 'W': pick[k] = winner
            else: pick[k] = loser

        flag = True
        for i in range(N):
            if rslt[i] == 'W':
                if pick[i] != winner:
                    flag = False
                    break
            else:
                if pick[i] != loser:
                    flag = False
                    break

        if flag:
            print("YES")
            print(''.join(pick))
        else:
            print("NO")