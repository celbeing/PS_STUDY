#23321: 홍익 댄스파티
import sys
input = sys.stdin.readline
dance = [list(input().rstrip()) for _ in range(5)]
state = [0]*len(dance[0])
ready = ['.','o','m','l','n']
jump = ['o','w','l','n','.']
sit = ['.','.','o','L','n']
for i in range(len(state)):
    if dance[0][i] == "o":
        state[i] = 1
    elif dance[1][i] == "o":
        state[i] = 0
    else:
        state[i] = 2

for i in range(len(state)):
    if state[i] == 0:
        for j in range(5):
            dance[j][i] = jump[j]

    elif state[i] == 1:
        for j in range(5):
            dance[j][i] = ready[j]

for i in range(5):
    print(''.join(dance[i]))