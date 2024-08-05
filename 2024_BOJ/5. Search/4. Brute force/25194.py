#25194: 결전의 금요일
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
M = [0]*7
for a in A: M[a%7] += 1
for i in range(7):
    if M[i] > 6: M[i] = 6
for a in range(M[1]+1):
    for b in range(M[2]+1):
        for c in range(M[3]+1):
            for d in range(M[4]+1):
                for e in range(M[5]+1):
                    for f in range(M[6]+1):
                        if (a+b*2+c*3+d*4+e*5+f*6)%7 == 4:
                            print("YES")
                            exit()
print("NO")