# J: 포닉스의 문단속
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
S = list(input().rstrip())
for i in range(N-1):
    if S[i] == 'A': continue
    k = ord('Z')-ord(S[i])+1
    if k <= K:
        K -= k
        S[i] = 'A'
k = ord(S[-1]) + K
while k > ord('Z'):
    k -= 26
S[-1] = chr(k)
print(''.join(S))