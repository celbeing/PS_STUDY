# 12025: 장난꾸러기 영훈
import sys
input = sys.stdin.readline
password = []
p = list(map(int,input().rstrip()))
check = []
for d in range(len(p)):
    if p[d] in [1,2,6,7]:
        check.append(d)
for k in range(1<<len(check)):
    pass
password.sort()
print(password[int(input())-1])