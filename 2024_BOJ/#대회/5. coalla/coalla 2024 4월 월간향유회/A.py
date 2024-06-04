# 17952: 과제는 끝나지 않아!
import sys
input = sys.stdin.readline
N = int(input())
task = []
score = []
result = 0
for _ in range(N):
    i = list(map(int,input().split()))
    if task:
        task[-1] -= 1
        if task[-1] == 0:
            task.pop()
            result += score.pop()
    if i[0] == 1:
        task.append(i[2])
        score.append(i[1])
if task:
    task[-1] -= 1
    if task[-1] == 0:
        task.pop()
        result += score.pop()
print(result)