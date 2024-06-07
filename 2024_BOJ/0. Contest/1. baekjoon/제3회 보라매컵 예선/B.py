#B: 사격
import sys
input = sys.stdin.readline
N,M,A = map(int,input().split())
score = list(map(int,input().split()))
score.sort()
score.append(1e9)
hands = [score[i] for i in range(N)]
hands.append(-1e9)
index = [i for i in range(N)]

for m in range(M):
	for i in range(N):
		while index[i] < N and hands[i] >= score[index[i]+1]:
			index[i] += 1
		hands[i] += score[index[i]]

for i in range(N):
    if hands[i] - score[i] >= A:
        print(score[i])
        exit()