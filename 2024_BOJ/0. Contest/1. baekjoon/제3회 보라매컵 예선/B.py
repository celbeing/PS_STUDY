#B: 사격
import sys
input = sys.stdin.readline

N,M,A = map(int,input().split())
S = sorted(list(map(int,input().split())))
S.append(int(1e11))

def check(k):
	get = 0
	s,e = 0,N
	while s < e:
		m = (s+e)//2
		if S[m] < k:
			if S[m+1] > k:
				s = m
				break
			s = m+1
		elif S[m] > k: e = m
		else:
			if S[m+1] == S[m]: s = m+1
			else:
				s = m
				break
	for n in range(M):
		while S[s] <= k: s += 1
		s -= 1
		if s < 0: break
		get += S[s]
		k += S[s]
	if get >= A: return True
	else: return False

s,e = 1,int(1e5+1)
while s < e:
	m = (s+e)//2
	if check(m): e = m
	else: s = m+1
print(e)