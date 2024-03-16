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
    wstnd = -1
    lstnd = -1
    for i in range(N):
        if rslt[i] == 'D': draw+=1
        elif rslt[i] == 'W':
            win+=1
            wstnd = i
        else:
            lose+=1
            lstnd = i

        if pick[i] == 'G': G+=1
        elif pick[i] == 'D': D+=1
        elif pick[i] == 'O': O+=1
        else: q.append(i)
    Q = len(q)

    if 0 < draw < N or ((G>0 and D>0 and O>0) and draw == 0) or win == N or lose == N:
        print("NO")
        continue
    if draw == N:
        if N == 2:
            print("NO")
        elif Q<3:
            if G+Q == N:
                while q:
                    pick[q.popleft()] = 'G'
            elif D+Q == N:
                while q:
                    pick[q.popleft()] = 'D'
            elif O+Q == N:
                while q:
                    pick[q.popleft()] = 'O'
            else:
                if Q == 1:
                    if D == 0:
                        pick[q.popleft()] = 'D'
                        D += 1
                    elif G == 0:
                        pick[q.popleft()] = 'G'
                        G += 1
                    elif O == 0:
                        pick[q.popleft()] = 'O'
                        O += 1
                    else:
                        pick[q.popleft()] = 'G'
                        G += 1
                    if G == 0 or D == 0 or O == 0:
                        print("NO")
                        continue
                elif Q == 2:
                    if D == 0:
                        pick[q.popleft()] = 'D'
                        D += 1
                    if G == 0:
                        pick[q.popleft()] = 'G'
                        G += 1
                    if q and O == 0:
                        pick[q.popleft()] = 'O'
                        O += 1
                    elif q:
                        pick[q.popleft()] = 'O'
                        O += 1
                    if G == 0 or D == 0 or O == 0:
                        print("NO")
                        continue
            print("YES")
            print(''.join(pick))
        else:
            print("YES")
            if G == 0:
                pick[q.popleft()] = 'G'
            if D == 0:
                pick[q.popleft()] = 'D'
            if O == 0:
                pick[q.popleft()] = 'O'
            while q:
                pick[q.popleft()] = 'G'
            print(''.join(pick))
        continue
    flag = True
    winner = ''
    if wstnd > 0:
        winner = pick[wstnd]
        if winner == 'G': losser = 'O'
        elif winner == 'O': losser = 'D'
        else: losser = 'G'
    else:
        losser = pick[lstnd]
        if pick[lstnd] == 'G': winner = 'D'
        elif pick[lstnd] == 'D': winner = 'O'
        else: winner = 'G'
    for i in range(N):
        if rslt[i] == 'W':
            if pick[i] == winner:
                continue
            elif pick[i] == '?':
                pick[i] = winner
            else:
                flag = False
                break
        else:
            if pick[i] == losser:
                continue
            elif pick[i] == '?':
                pick[i] = losser
            else:
                flag = False
                break
    if flag:
        print("YES")
        print(''.join(pick))
    else:
        print("NO")