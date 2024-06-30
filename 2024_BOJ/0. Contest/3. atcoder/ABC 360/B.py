import sys
input = sys.stdin.readline
S,T = map(str,input().split())
for i in range(1,len(S)):
    for j in range(i):
        vert = ""
        t = 0
        while i*t+j < len(S):
            vert += S[i*t+j]
            t += 1
        if vert == T:
            print("Yes")
            exit()
print("No")