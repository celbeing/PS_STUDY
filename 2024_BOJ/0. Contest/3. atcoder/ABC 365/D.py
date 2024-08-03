import sys
input = sys.stdin.readline
N = int(input())
S = list(input().rstrip())
win = [0]*N
drw = [0]*N
win[0] = 1
for i in range(1,N):
    if S[i] == S[i-1]:
        win[i] = drw[i-1]+1
        drw[i] = win[i-1]
    if S[i-1] == "R":
        if S[i] == "P":
            win[i] = max(win[i-1]+1,drw[i-1]+1)
            drw[i] = drw[i-1]
        elif S[i] == "S":
            win[i] = win[i-1]+1
            drw[i] = max(win[i-1],drw[i-1])
    elif S[i-1] == "P":
        if S[i] == "S":
            win[i] = max(win[i-1]+1,drw[i-1]+1)
            drw[i] = drw[i-1]
        elif S[i] == "R":
            win[i] = win[i-1]+1
            drw[i] = max(win[i-1],drw[i-1])
    else:
        if S[i] == "R":
            win[i] = max(win[i-1]+1,drw[i-1]+1)
            drw[i] = drw[i-1]
        elif S[i] == "P":
            win[i] = win[i-1]+1
            drw[i] = max(win[i-1],drw[i-1])
print(max(win[-1],drw[-1]))