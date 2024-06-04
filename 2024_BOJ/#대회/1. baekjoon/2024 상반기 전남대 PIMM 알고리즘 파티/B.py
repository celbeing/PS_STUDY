#B: 전주 듣고 노래 맞히기
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
notes = dict()
scale = "CDEFGAB"

def note(k):
    r = 0
    r += scale.index(k[0])*100
    r += scale.index(k[1])*10
    r += scale.index(k[2])
    return r

for _ in range(N):
    music = list(input().split())
    f = note(music[2:5])
    if f in notes:
        notes[f] = "?"
    else:
        notes[f] = music[1]
for _ in range(M):
    ask = note(list(input().split()))
    if ask in notes:
        print(notes[ask])
    else:
        print("!")