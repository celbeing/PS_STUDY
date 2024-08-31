#1268: 임시 반장 정하기
import sys
input = sys.stdin.readline
stud = int(input())
clas = [list(map(int,input().split())) for _ in range(stud)]
mate = [0]*stud
high = 0
for i in range(stud):
    for j in range(i+1,stud):
        for k in range(5):
            if clas[i][k] == clas[j][k]:
                mate[i] += 1
                mate[j] += 1
                break
    if high < mate[i]:
        high = mate[i]
print(mate.index(high)+1)