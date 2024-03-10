#I: 올라올라
import sys
input = sys.stdin.readline

last = 0
peek = 0
len = 1

N=int(input())
A=list(map(int,input().split()))
A.append(1e9)

for i in range(1,N+1):
	if A[i] >= A[peek]:
		last = peek
		peek = i
		if len < peek - last:
			len = peek - last

print(len)