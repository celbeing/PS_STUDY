#9057: ACM-UCPC
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    rank = []
    s_count = {}
    s_limit = {}
    r_count = {}
    for _ in range(int(input())):
        team,school,solved,penalty = map(str,input().split())
        rank.append((team, school, int(solved), int(penalty)))
        s_count[school] = s_count.get(school,0) + 1
    for school in s_count.keys():
        s_limit[school] = (s_count[school]+1)//2
    rank.sort(key = lambda x: (x[2], -x[3]))
    drop = []
    draft = []
    r = 0
    while rank:
        tm,sc,s,p = rank.pop()
        if r_count.get(sc,0) == s_limit[sc]: drop.append((tm,sc,s,p))
        elif r < 10 and r_count.get(sc,0) > 3: drop.append((tm,sc,s,p))
        elif 10 <= r < 20 and r_count.get(sc,0) > 2: drop.append((tm,sc,s,p))
        elif 20 <= r < 30 and r_count.get(sc,0) > 1: drop.append((tm,sc,s,p))
        elif 30 <= r and r_count.get(sc,0) > 0: drop.append((tm,sc,s,p))
        else:
            draft.append((tm,sc,s,p))
            r_count[sc] = r_count.get(sc,0)+1
        if len(draft) == 60: break
        r += 1
    drop.reverse()
    while drop and len(draft) < 60:
        draft.append(drop.pop())
    draft.sort(key = lambda x: (-x[2], x[3]))
    print(draft[-1][0])