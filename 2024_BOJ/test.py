table = dict()
N = int(input())
for i in range(N):
	A, B = map(str, input().split())
	table[A] = B
M = int(input())
for i in range(M):
	C = input()
	print(table[C])
