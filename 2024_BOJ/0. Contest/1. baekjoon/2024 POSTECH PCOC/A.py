# A: 글로벌 포닉스
import sys
input = sys.stdin.readline
s1 = input().rstrip()
s2 = input().rstrip()
s3 = input().rstrip()
l = False
k = False
p = False
if s1[0] == 'l': l = True
elif s1[0] == 'k': k = True
elif s1[0] == 'p': p = True

if s2[0] == 'l': l = True
elif s2[0] == 'k': k = True
elif s2[0] == 'p': p = True

if s3[0] == 'l': l = True
elif s3[0] == 'k': k = True
elif s3[0] == 'p': p = True

if l and p and k: print("GLOBAL")
else: print("PONIX")